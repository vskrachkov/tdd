"""
    functional_tests.py
    ===================
"""
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django import setup
from django.test import LiveServerTestCase

from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlists.settings")
setup()

fake = Faker()


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        """Starts Chrome web browser."""
        self.browser = webdriver.Chrome(
            executable_path='/usr/local/bin/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """Close Chrome web browser."""
        self.browser.quit()

    def check_row_in_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == row_text for row in rows))

    @staticmethod
    def types_item_text_and_press_enter(self, input_box):
        sentence = fake.sentence(nb_words=5)
        input_box.send_keys(sentence)
        input_box.send_keys(Keys.ENTER)
        return sentence

    def assert_current_url_regex(self, expression):
        """Fails if current url is not match :expression:
        Args:
            :expression: regular expression for matching current url.
        """
        self.assertRegex(self.browser.current_url, expression)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # (1) Go to the home page.
        self.browser.get(self.live_server_url)

        # (2) Checks that tab title and page header contain right string.
        self.assertIn('To-Do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header)

        # (3) Checks that placeholder of input box for to-do items contains
        # right invite message.
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual('Enter a to-do item',
                         input_box.get_attribute('placeholder'))

        # (4) Is typing an item text into input box and press Enter.
        first_user_item_text = self.types_item_text_and_press_enter(input_box)

        # (5) Checks that redirect url corresponds to right regular expression.
        self.assert_current_url_regex('/lists/.+')

        # (6) The first user leaves the site and another comes.
        self.browser.quit()
        self.browser = webdriver.Chrome()
        self.browser.get(self.live_server_url)

        # (7) Checks that another user cannot see the text of first one.
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn(first_user_item_text, page_text)

        # {same as 4} Another user types a text of new item and press Enter.
        another_user_text = self.types_item_text_and_press_enter(input_box)
        # {same as 5} Checks that redirect url corresponding to right
        self.assert_current_url_regex('/lists/.+')
        # expression and not equal to firs user url.

        self.fail('The test is not finished !')
