"""
    Module contains base classes for functional test.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import os

from django import setup
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlists.settings")
        setup()
        super(FunctionalTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(FunctionalTest, cls).tearDownClass()
    
    def setUp(self):
        """Starts Chrome web browser."""
        self.browser = webdriver.Chrome(
            executable_path='/usr/local/bin/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """Close Chrome web browser."""
        self.browser.quit()

    def check_row_in_table(self, row_text):
        """Checks that any row in table with to-do list items contains
        :row_text: parameter.
        """
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == row_text for row in rows))

    def assert_current_url_regex(self, expression):
        """Fails if current url is not match :expression:
        Args:
            :expression: regular expression for matching current url.
        """
        self.assertRegex(self.browser.current_url, expression)
