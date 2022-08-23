from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):  
        self.browser = webdriver.Edge()

    def tearDown(self):  
        self.browser.quit()

    # Helper method
    # gets table, rows and puts them in an array
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

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

        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')  
        # self.assertTrue(
        # any(row.text == '1: Buy peacock feathers' for row in rows),
        # f"New to-do item did not appear in table. Contents were:\n{table.text}"
        # )
        # self.assertIn('1: Buy peacock feathers', [row.text for row in rows])     
       
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        # test 2 - Add a second input to the table
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # -- The page updates again, and now shows both items on her list
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        # self.assertIn(
        # '2: Use peacock feathers to make a fly',
        #  [row.text for row in rows]
        # )
        
        # if check for row method is equals to (x)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        self.fail('Finish the test!')

if __name__ == '__main__':  
    unittest.main()