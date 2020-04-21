import requests
from lxml import html
from bs4 import BeautifulSoup

class Task:
    def __init__(self, url, name, type):
        self.url = url
        self.name = name
        self.type = type
        self.id = 0

    def set_id(self, id):
        self.id = id
    def print_task_data(self):
        print(f"TASK (TYPE={self.type}): \"{self.name}\", ID: {self.id} (URL: {self.url})")

class Course:
    def __init__(self, url, name):
        self.url = url
        self.name = name
        self.id = 0
        self.tasks = []

    def set_id(self, id):
        self.id = id
    def add_task(self, task):
        self.tasks.append(task) # task is Task() object
    def print_course_data(self):
        print(f"COURSE: \"{self.name}\", ID: {self.id} (URL: {self.url})")
