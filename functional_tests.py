"""
    functional_tests.py
    ===================
"""

import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    """"""

    def setUp(self):
        """Starts Chrome web browser."""
        self.browser = webdriver.Chrome(
            executable_path='/usr/local/bin/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """Close Chrome web browser."""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """User Story::

            User notices that the page title and its header contains 'To-Do'
        string.
            He invited to create new to-do item straight away. He types a
        text of to-do item into a textbox. When he press enter page updates
        and he sees the list with item that contains a text that he write
        before.
            There is still a textbox here. He types a text of a new item
        and hit enter. The page updates again and there two items of list
        displayed now.
            Then he sees that site generate an unique URL for he -- there
        is some explanatory text for this effect. He visit the URl
        and his to-do list still here. User goes from site.
        """
        # TODO: docs must comply with the code of test.
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Test not working !')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
