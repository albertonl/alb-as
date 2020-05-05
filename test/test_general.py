import pytest
import time

from src.scraper import main as scraper

from src.util import auth, course_scraper, emailer, versions

def test_main():
    assert scraper(start_time=time.time(),testing=True)
