import os
import sys
import time
import unittest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.form_page import FormPage
from parameterized import parameterized, parameterized_class

CHROME_EXECUTABLE_PATH ="/usr/lib/chromium-browser/chromedriver"

DATA_SET = [("Online Consumer Trends 2020",), ("The Ultimate Guide to Headless Commerce",),("Zero Party Data revolution in Ecommerce",),]


class TestSearchEbook(unittest.TestCase):
    
    TEST_NAME = "Maciej Duda"
    TEST_EMAIL = "maciej.duda+testrekrutacja@salesmanago.com"
    TEST_COMPANY = "salesmanago"
    TEST_PHONE = "555555555"
    TEST_SITE = "www.salesmanago.pl"

    #EBOOK = "Online Consumer Trends 2020"
    def setUp(self):
        
        self.driver = webdriver.Chrome(CHROME_EXECUTABLE_PATH)
        self.driver.maximize_window()
        self.driver.get("https://www.salesmanago.com/")
        self.form_page = FormPage(self.driver)
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

    def tearDown(self):
        self.driver.quit()

    @parameterized.expand(DATA_SET)
    def test_download_ebook(self, ebook_name):
        all_ebooks= self.driver.find_elements(By.CLASS_NAME, 'ebook__img--container')
        # print(ebook_name, "EBOOK NAME")

        for ebook in all_ebooks:
            time.sleep(3)
            ebook.click()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            title = self.driver.find_element(By.CLASS_NAME, 'ebook__title')
            # print(title.text.strip().replace("\n", " "))
            if title.text.strip().replace("\n", " ") == ebook_name:
                print("Ebook found")
                self.form_page.fill_form(self.TEST_NAME,self.TEST_EMAIL,self.TEST_COMPANY,self.TEST_PHONE,self.TEST_SITE)
                self.form_page.download_file(ebook_name)
                break

            else:
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
        
        assert self.form_page.is_file_download(ebook_name) is True

        
        

if __name__ == '__main__':
   
    unittest.main()
