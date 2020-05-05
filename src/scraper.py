import os
import time
import requests
from lxml import html
from bs4 import BeautifulSoup

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .models import Task, Course
from .util import auth, course_scraper, emailer, versions # if you are cloning, add auth.py yourself with your data (more info in util/README.md)

engine = create_engine(os.getenv("DATABASE_URL")) # mine is set to 'sqlite:///db.sqlite3'
db = scoped_session(sessionmaker(bind=engine))

def main(start_time, testing=False):
    payload = {
        "username": auth.username,
        "password": auth.password,
        "logintoken": None
    }

    session_requests = requests.session() # initialize session object

    # log in
    login_url = versions.get_login_url(version="default")
    res = session_requests.get(login_url)

    if res.status_code != requests.codes.ok:
        raise RuntimeError(f"Login GET request returned HTTP {res.status_code}")
    tree = html.fromstring(res.text)
    auth_token = list(set(tree.xpath("//input[@name='logintoken']/@value")))[0] # get logintoken
    payload["logintoken"] = auth_token # store logintoken

    # send post request to log in
    result = session_requests.post(
        login_url,
        data = payload,
        headers = dict(referer=login_url)
    )

    if result.status_code != requests.codes.ok:
        raise RuntimeError(f"Login POST request returned HTTP {result.status_code}")

    print("Login successful")

    # scrape courses
    courses = [] # initialize empty course list
    for course in course_scraper.find_courses(session=session_requests):
        courses.append(Course(url=course[0], name=course[1]))
        courses[len(courses)-1].set_id(course_scraper.get_id(url=course[0])[0])
        courses[len(courses)-1].print_course_data()

    # scrape and add tasks to course
    for course in courses:
        print()
        course.print_course_data()
        print("Analyzing...")
        for task in course_scraper.find_tasks(session=session_requests, url=versions.convert_url(url=course.url,mode="auto")):
            task_obj = Task(url=task[0],name=task[1],type=task[2])
            task_obj.set_id(course_scraper.get_id(url=task[0])[0])
            task_obj.print_task_data()
            course.add_task(task_obj)

    # check records
    new_courses = [] # (new courses)
    new_tasks = [] # (new tasks)
    print()
    print("Comparing to records from database...")
    for course in courses:
        db_course = db.execute("SELECT * FROM courses WHERE cid = :cid",
            {"cid": course.id}).fetchone()

        if not db_course:
            print("NEW", end=" ")
            course.print_course_data()
            if not testing:
                db.execute("INSERT INTO courses (cid, cname, curl) VALUES (:cid, :cname, :curl)",
                    {"cid": course.id, "cname": course.name, "curl": course.url})
                db.commit()
            new_courses.append(course.id)

        for task in course.tasks:
            db_task = db.execute("SELECT * FROM tasks WHERE tid = :tid",
                {"tid": task.id}).fetchone()

            if not db_task:
                print("NEW", end=" ")
                task.print_task_data()
                if not testing:
                    db.execute("INSERT INTO tasks (tid, tname, turl, type, cid_fk) VALUES (:tid, :tname, :turl, :type, :cid_fk)",
                        {"tid": task.id, "tname": task.name, "turl": task.url, "type": task.type, "cid_fk": course.id})
                    db.commit()
                new_tasks.append(task.id)

    emailer.emailer(db=db,
        new_courses=new_courses,
        new_tasks=new_tasks,
        start_time=start_time,
        testing=True if testing else False
    )
    if testing:
        # if it reached this point, well enough as to return True
        return True

if __name__ == '__main__':
    start_time = time.time()
    main(start_time)
    print("Scraped all courses in %s seconds" % (time.time() - start_time))
