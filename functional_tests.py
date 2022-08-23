from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):  
        self.browser = webdriver.Edge()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Goes to homepage
        self.browser.get('http://localhost:8000')
        # Title page and header mention To-Do
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('To-Do', header_text)
        # Enter a To-Do item
        inputbox = self.browser.find_element_by_id('id_new_item')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # input
        inputbox.send_keys('Buy peacock feathers')
        # Hit Enter and wait 1 second
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1)  
        # The table should list 1: Buy peacock feathers
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')  
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # Still to complete, add another item
        self.fail('Finish the test!')
        # Page updates again and we see both items in the table list

if __name__ == '__main__':  
    unittest.main()