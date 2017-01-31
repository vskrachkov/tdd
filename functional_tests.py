"""
    functional_tests.py
    ===================
"""
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django import setup
from django.test import LiveServerTestCase

from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlists.settings")
setup()

TEST_PORT = 8081
fake = Faker()


class NewVisitorTest(LiveServerTestCase):
    """"""

    def setUp(self):
        """Starts Chrome web browser."""
        self.browser = webdriver.Chrome(
            executable_path='/usr/local/bin/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """Close Chrome web browser."""
        time.sleep(2)
        self.browser.quit()

    def check_row_in_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == row_text for row in rows))

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(f'http://localhost:{TEST_PORT}')
        self.assertIn('To-Do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header)
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual('Enter a to-do item',
                         input_box.get_attribute('placeholder'))
        item_text = fake.sentence(nb_words=5)
        input_box.send_keys(item_text)
        # When he hits enter, a page updates and contains the text that he
        # write before.
        input_box.send_keys(Keys.ENTER)

        # There is still a textbox here. He types a text of a new item
        # and hit enter. The page updates again and there two items of list
        # displayed now.
        # Then he sees that site generate an unique URL for he -- there
        # is some explanatory text for this effect. He visit the URl
        # and his to-do list still here. User goes from site.
        self.fail('Test not finished !')
