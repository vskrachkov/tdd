"""
    functional_tests.py
    ===================
"""

from selenium import webdriver


browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title, browser.quit()
browser.quit()
