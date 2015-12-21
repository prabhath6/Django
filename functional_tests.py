__author__ = 'prabhath'

from selenium import webdriver

# Checking if the browser contains "Django" in its title.
browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title

