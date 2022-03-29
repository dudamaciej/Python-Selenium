import os
import sys
import time
import unittest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from parameterized import parameterized, parameterized_class


class FormPage() :
    NAME_INPUT = '//*[@id="uspForm"]/div[1]/div[1]/div/input'
    EMAIL_INPUT =  '//*[@id="email"]'
    COMPANY_INPUT =  '//*[@id="company"]/div/input'
    PHONE_INPUT =  '//*[@id="phoneNumber"]'
    SITE_INPUT =  '//*[@id="uspForm"]/div[1]/div[4]/div/input'
    GET_EBOOK_BUTTON = '//*[@id="uspForm"]/div[2]/div/button'

    TEST_NAME = "Maciej Duda"
    TEST_EMAIL = "maciej.duda+testrekrutacja@salesmanago.com"
    TEST_COMPANY = "salesmanago"
    TEST_PHONE = "555555555"
    TEST_SITE = "www.salesmanago.pl"

    def fill_form(self, ebook):
        self.driver.find_element (By.XPATH, FormPage.NAME_INPUT).send_keys (FormPage.TEST_NAME)
        self.driver.find_element (By.XPATH, FormPage.EMAIL_INPUT).send_keys (FormPage.TEST_EMAIL)
        self.driver.find_element (By.XPATH, FormPage.COMPANY_INPUT).send_keys (FormPage.TEST_COMPANY)
        self.driver.find_element (By.XPATH, FormPage.PHONE_INPUT).send_keys (FormPage.TEST_PHONE)
        self.driver.find_element (By.XPATH, FormPage.SITE_INPUT).send_keys (FormPage.TEST_SITE)
        self.driver.find_element (By.XPATH, FormPage.GET_EBOOK_BUTTON).click ()
        time.sleep (5)
        ebook_btn = self.driver.find_element (By.XPATH, '//a[contains(text(),"HERE")]')
        ebook_link = ebook_btn .get_attribute ("href")
        r = requests.get (ebook_link, allow_redirects=True)

        open (os.path.join (os.path.dirname (__file__), "download", ebook + ".pdf"), 'wb').write (r.content)

        is_file = os.path.isfile (os.path.join (os.path.dirname (__file__), "download", ebook + ".pdf"))

        assert is_file

        # self.driver.find_element (By.XPATH, '//a[contains(text(),"HERE")]').click ()
        time.sleep (10)