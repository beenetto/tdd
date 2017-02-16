from selenium import webdriver
import unittest


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
        self.assertIn('To-Do lists', self.browser.title)

        # User invited to enter a to-do list item straight away

        # User types "My to do" into the textbox

        # When user hits ENTER, the page updates
        # "1: My to-do" as an item in the to-do list

        # There is still a textbox inviting the user to add an other item.
        # User enters "My second to do"

        # Page updates again and shows both items

        # User notices that there is a unique url generated

        # User visits that URL and sees that the enered
        # items are still in the list

        # User finishes


if __name__ == '__main__':
    unittest.main()
