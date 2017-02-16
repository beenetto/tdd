import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.http import HttpRequest



class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # USER visits homepage
        self.browser.get('http://localhost:8000')

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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: My to-do' for row in rows),
            'New to-do item did not appear in the table'
        )

        # There is still a textbox inviting the user to add an other item.
        # User enters "My second to do"
        self.fail('Finish the test!')

        # Page updates again and shows both items

        # User notices that there is a unique url generated

        # User visits that URL and sees that the enered
        # items are still in the list

        # User finishes

    def test_home_page_can_test_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'


if __name__ == '__main__':
    unittest.main()
