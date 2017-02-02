"""
    Tests creation of simple todo lists.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from faker import Faker

from .base import FunctionalTest

fake = Faker()


class NewVisitorTest(FunctionalTest):
    @staticmethod
    def types_item_text_and_press_enter(input_box):
        sentence = fake.sentence(nb_words=5)
        input_box.send_keys(sentence)
        input_box.send_keys(Keys.ENTER)
        return sentence

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
        self.browser = webdriver.Chrome(
            executable_path='/usr/local/bin/chromedriver')
        self.browser.get(self.live_server_url)

        # (7) Checks that another user cannot see the text of first one.
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn(first_user_item_text, page_text)

        # {same as 4} Another user types a text of new item and press Enter.
        input_box = self.browser.find_element_by_id('id_new_item')
        another_user_text = self.types_item_text_and_press_enter(input_box)
        # {same as 5} Checks that redirect url corresponding to right
        self.assert_current_url_regex('/lists/.+')
        # expression and not equal to firs user url.
