import os
import sys
import time
import unittest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from parameterized import parameterized, parameterized_class
from page_objects.form_page import FormPage
@parameterized_class([
    {"ebook": "Zero-Party Data Revolution Essentials"},
   {"ebook": "Online Consumer Trends 2020"},
   {"ebook": "The Ultimate Guide to Headless Commerce"},
])

class SearchEbook(unittest.TestCase):
    EBOOK = "Online Consumer Trends 2020"
    def setUp(self):
        print ('searching for:', self.ebook)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window ()
        self.driver.get("https://www.salesmanago.com/")
        cookies_accept = self.driver.find_element(By.ID, 'close-cookies')
        if cookies_accept:
            cookies_accept.click()
        # menu
        self.driver.find_element(By.XPATH, '/html/body/nav[2]/div/div/ul[1]/li[4]').click()
        self.driver.find_element(By.XPATH, '/html/body/nav[2]/div/div/ul[1]/li[4]/div/div/div[1]/div/ul/a[1]').click()
        time.sleep(3)

        # close live chat
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, '//*[@id="hubspot-messages-iframe-container"]/iframe'))
        self.driver.find_element(By.XPATH, '/html/body/div/div[1]/span/div/button').click()
        self.driver.find_element(By.XPATH, '/html/body/div/div[1]/span/div/button').click()
        self.driver.switch_to.default_content()

    def test_download_ebook(self):
        all_ebooks= self.driver.find_elements(By.CLASS_NAME, 'ebook__img--container')


        for ebook in all_ebooks:
            time.sleep(3)
            ebook.click()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            title = self.driver.find_element(By.CLASS_NAME, 'ebook__title')
            if title.text.strip().replace("\n", " ") == self.ebook:
                print("Ebook found")
                FormPage.fill_form(self,self.ebook)
                self.driver.close()
                break

            else:
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])

    def tearDown(self):

        self.driver.quit()

if __name__ == '__main__':
    if len (sys.argv) > 1:
        SearchEbook.EBOOK = sys.argv.pop()
    unittest.main()
