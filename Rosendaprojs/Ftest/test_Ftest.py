from selenium import webdriver
import unittest

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time

class PageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    
    def test_start_list_and_retrieve(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Belleza', self.browser.title)
        headerText = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Belleza - Contact Us', headerText)

        BellezaName = self.browser.find_element_by_id('belleza_Name')
        self.assertEqual(BellezaName.get_attribute('placeholder'),'Enter your name here.')
        BellezaName.send_keys('Rosenda Madriaga')
        time.sleep(1)

        BellezaEmail = self.browser.find_element_by_id('belleza_Email')
        self.assertEqual(BellezaEmail.get_attribute('placeholder'),'Enter your e-mail here.')
        BellezaEmail.send_keys('rosenda.madriaga@gmail.com')
        time.sleep(0.5)

        BellezaAddress = self.browser.find_element_by_id('belleza_Address')
        self.assertEqual(BellezaAddress.get_attribute('placeholder'),'Enter your address here.')
        BellezaAddress.send_keys('Datu Esmael Dasmarinas Cavite')
        time.sleep(0.5)

        BellezaConcern = self.browser.find_element_by_id('belleza_Concern')
        self.assertEqual(BellezaConcern.get_attribute('placeholder'),'Choose your concern.')
        BellezaselectClientConcern = Select(BellezaConcern)
        BellezaselectClientConcern.select_by_visible_text('Question')
        time.sleep(0.5)

        BellezaReview = self.browser.find_element_by_id('belleza_ConcernText')
        self.assertEqual(BellezaReview.get_attribute('placeholder'),'Enter message here.')
        BellezaReview.send_keys('How can I order?')
        time.sleep(0.5)
            
        btnSubmit = self.browser.find_element_by_id('btnSubmit')
        btnSubmit.click()
        time.sleep(0.5)

        self.browser.get(self.live_server_url)
        self.assertIn('Belleza', self.browser.title)
        headerText = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Belleza - Contact Us', headerText)

        BellezaName = self.browser.find_element_by_id('belleza_Name')
        self.assertEqual(BellezaName.get_attribute('placeholder'),'Enter your name here.')
        BellezaName.send_keys('Joselle Sacriz')
        time.sleep(1)

        BellezaEmail = self.browser.find_element_by_id('belleza_Email')
        self.assertEqual(BellezaEmail.get_attribute('placeholder'),'Enter your e-mail here.')
        BellezaEmail.send_keys('joselle.sacriz@gmail.com')
        time.sleep(0.5)

        BellezaAddress = self.browser.find_element_by_id('belleza_Address')
        self.assertEqual(BellezaAddress.get_attribute('placeholder'),'Enter your address here.')
        BellezaAddress.send_keys('Area 1 Dasmarinas Cavite')
        time.sleep(0.5)

        BellezaConcern = self.browser.find_element_by_id('belleza_Concern')
        self.assertEqual(BellezaConcern.get_attribute('placeholder'),'Choose your concern.')
        BellezaselectClientConcern = Select(BellezaConcern)
        BellezaselectClientConcern.select_by_visible_text('Order Complaints')
        time.sleep(0.5)

        BellezaReview = self.browser.find_element_by_id('belleza_ConcernText')
        self.assertEqual(BellezaReview.get_attribute('placeholder'),'Enter message here.')
        BellezaReview.send_keys('Issue about my ordered clothes.')
        time.sleep(0.5)
            
        btnSubmit = self.browser.find_element_by_id('btnSubmit')
        btnSubmit.click()
        time.sleep(0.5)
        
        # inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_tag_name('table')
        belleza_rowdata = table.find_elements_by_tag_name('tr')
        self.assertIn('Entry 1: Rosenda Madriaga, rosenda.madriaga@gmail.com, Datu Esmael Dasmarinas Cavite, Question, How can I order?', [row.text for row in belleza_rowdata])
        self.assertIn('Entry 2: Joselle Sacriz, joselle.sacriz@gmail.com, Area 1 Dasmarinas Cavite, Order Complaints, Issue about my ordered clothes.', [row.text for row in belleza_rowdata])
        
if __name__ == '__main__' :
    unittest.main(warnings='ignore')
