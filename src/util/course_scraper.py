import requests
from lxml import html
from bs4 import BeautifulSoup

import urllib.parse as urlparse
from urllib.parse import parse_qs

task_types = [
    'forum',
    'assign',
    'resource',
    'url',
    'page'
    'dialogue',
    'quiz'
]

def find_courses(session):
    """ Finds all active courses in your dashboard and returns a list with the names and corresponding URLs """
    # retrieve request data
    dashboard_url = 'https://aules2.edu.gva.es/moodle/my/'
    res = session.get(dashboard_url)
    soup = BeautifulSoup(res.content, 'html.parser')

    # initialize empty course list
    courses = []

    # find all instances of courses
    for raw_course in soup.find_all('td', class_='cell c1'):
        for a in raw_course.find_all('a', href=True):
            courses.append([a['href'], a.get_text()]) # course structure (list):
                                                      # ["<URL_FOR_COURSE>", "<COURSE_NAME>"]

    return courses

def get_id(url):
    """
        Returns the ID of a course or a task given the URL.
        URL structure: https://aules2.edu.gva.es/moodle/course/view.php?id=XXXXX
    """
    parsed = urlparse.urlparse(url)
    return parse_qs(parsed.query)['id']

def find_tasks(session, url):
    """ Returns a list of tasks given the course URL. """
    res = session.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    # initialize empty task lists
    tasks = []
    aux = {
        'type': '',
        'url': '',
        'name': ''
    }
    
    # find all instances of tasks in a course's page
    for type in task_types:
        # get tasks with specific type
        aux['type'] = type
        for task in soup.find_all('li', class_=f'activity {type} modtype_{type}'):
            # got all tasks with type 'type'. Now, get the task URLs
            a = task.find_all('a', href=True)
            aux['url'] = a[0]['href']
            print(a[0]['href'], end=" ")

            # get task name
            span = task.find_all('span', class_='instancename')
            aux['name'] = span[0].get_text().rsplit(' ', 1)[0]

            tasks.append([aux['url'], aux['name'], aux['type']])

    return tasks
