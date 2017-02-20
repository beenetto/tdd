from contextlib import contextmanager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of

from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    @contextmanager
    def wait_for_page_load(self, timeout=30):
        old_page = self.browser.find_element_by_tag_name('html')
        yield WebDriverWait(
            self.browser, timeout).until(staleness_of(old_page))


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # USER visits homepage
        self.browser.get(self.live_server_url)

        # User sees "Django" in the page title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User invited to enter a to-do list item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # User types "My to-do" into the textbox
        inputbox.send_keys('My to-do')

        # When user hits ENTER, the page updates
        # "1: My to-do" as an item in the to-do list
        inputbox.send_keys(Keys.ENTER)

        with self.wait_for_page_load(timeout=10):
            self.check_for_row_in_list_table('1: My to-do')
            user_list_url = self.browser.current_url
            self.assertRegex(user_list_url, '/lists/.+')

        # There is still a textbox inviting the user to add an other item.
        # User enters "My second to do"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('My to-do')
        inputbox.send_keys(Keys.ENTER)

        # Page updates again and shows both items
        with self.wait_for_page_load(timeout=10):
            self.check_for_row_in_list_table('1: My to-do')
            self.check_for_row_in_list_table('2: My to-do')

        # A new user comes along
        ## We use a new browser session to make sure that
        ## no information leaks to other users

        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('1: My to-do', page_text)
        self.assertNotIn('2: My to-do', page_text)

        # The new user starts a new list by entering a new item.

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy something')
        inputbox.send_keys(Keys.ENTER)

        # New user gets his own URL
        with self.wait_for_page_load(timeout=10):
            new_user_list_url = self.browser.current_url
            self.assertRegex(new_user_list_url, '/lists/.+')
            self.assertNotEqual(new_user_list_url, user_list_url)

        # Check again that diferent user list are not mixed up
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('1: My to-do', page_text)
        self.assertIn('Buy something', page_text)

        # Satisfied


if __name__ == '__main__':
    unittest.main()
