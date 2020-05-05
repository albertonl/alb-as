import pytest
import requests
import time

from lxml import html
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from src.util import auth, course_scraper, emailer, versions

def login_session():
    payload = {
        "username": auth.username,
        "password": auth.password,
        "logintoken": None
    }

    session_requests = requests.session()

    login_url = versions.get_login_url(version="default")
    res = session_requests.get(login_url)

    if res.status_code != requests.codes.ok:
        raise RuntimeError(f"Login GET request returned HTTP {res.status_code} (testing)")
    tree = html.fromstring(res.text)
    auth_token = list(set(tree.xpath("//input[@name='logintoken']/@value")))[0] # get logintoken
    payload["token"] = auth_token # store logintoken

    # send post request to log in
    result = session_requests.post(
        login_url,
        data = payload,
        headers = dict(referer=login_url)
    )

    if res.status_code != requests.codes.ok:
        raise RuntimeError(f"Login POST request returned HTTP {res.status_code} (testing)")
    return session_requests

def db_config():
    engine = create_engine("sqlite:///src/db.sqlite3")
    return scoped_session(sessionmaker(bind=engine)) # db

##### TESTS #####
def test_courses():
    session = login_session()
    # assert course list is not empty
    assert course_scraper.find_courses(session=session) != []

def test_tasks():
    session = login_session()
    # TODO: search directly on db for a course with tasks:
    # 1. task = SELECT * FROM tasks LIMIT 1
    # 2. SELECT * FROM courses WHERE cid = {task['cid_fk']}
    # But first, task/course deletion is needed, as to avoid
    # attempting a test on a course that no longer exists.
    courses = course_scraper.find_courses(session=session)
    # assert task list is not empty
    # NOTE: this test MAY fail if the course on courses[0][0] has no
    # tasks or does no longer exist.
    assert course_scraper.find_tasks(session=session,url=courses[0][0])

def test_get_id():
    # test with example url
    url = 'https://example.com/a/very/long/url/path?id=59012'
    assert course_scraper.get_id(url)[0] == '59012'

def test_emailer():
    db = db_config()
    # 5 example courses from db
    new_courses = []
    courses_db = db.execute("SELECT cid FROM courses LIMIT 5").fetchall()
    for course in courses_db:
        new_courses.append(course['cid'])

    # 5 example tasks from db
    new_tasks = []
    tasks_db = db.execute("SELECT tid FROM tasks LIMIT 5").fetchall()
    for task in tasks_db:
        new_tasks.append(task['tid'])

    # get generated email text
    email_text = emailer.emailer(
        db = db,
        new_courses = new_courses,
        new_tasks = new_tasks,
        start_time = time.time(),
        testing = True
    )
    assert "NEW COURSE" in email_text and "NEW TASK" in email_text
