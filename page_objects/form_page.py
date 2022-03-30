import os
import time
import requests
from selenium.webdriver.common.by import By


class FormPage:

    NAME_INPUT = '//*[@id="uspForm"]/div[1]/div[1]/div/input'
    EMAIL_INPUT =  '//*[@id="email"]'
    COMPANY_INPUT =  '//*[@id="company"]/div/input'
    PHONE_INPUT =  '//*[@id="phoneNumber"]'
    SITE_INPUT =  '//*[@id="uspForm"]/div[1]/div[4]/div/input'
    GET_EBOOK_BUTTON = '//*[@id="uspForm"]/div[2]/div/button'
    HERE_BUTTON = '//a[contains(text(),"HERE")]'

    def __init__(self, driver):
        self.driver = driver

    def type_name(self, name: str) -> None:
        self.driver.find_element(By.XPATH, self.NAME_INPUT).send_keys(name)

    def type_email(self, email: str) -> None:
        self.driver.find_element(By.XPATH, self.EMAIL_INPUT).send_keys(email)

    def type_company(self, company: str) -> None:
        self.driver.find_element(By.XPATH, self.COMPANY_INPUT).send_keys(company)

    def type_phone(self, phone: str) -> None:
        self.driver.find_element(By.XPATH, self.PHONE_INPUT).send_keys(phone)

    def type_site(self, website: str) -> None:
        self.driver.find_element(By.XPATH, self.SITE_INPUT).send_keys(website)

    def download_file(self, ebook) -> None:
        ebook_btn = self.driver.find_element (By.XPATH, self.HERE_BUTTON)
        time.sleep (5)
        ebook_link = ebook_btn .get_attribute ("href")
        r = requests.get (ebook_link, allow_redirects=True)

        open(os.path.join (os.path.dirname(os.path.dirname (__file__)), "download", ebook + ".pdf"), 'wb').write(r.content)

    def is_file_download(self, ebook) -> None:
        is_file = os.path.isfile(os.path.join (os.path.dirname(os.path.dirname (__file__)), "download", ebook + ".pdf"))
        return is_file

    def fill_form(self, name: str, email: str, company: str, phone: str, website: str):
        self.type_name(name)
        self.type_email(email)
        self.type_company(company)
        self.type_phone(phone)
        self.type_site(website)
        self.driver.find_element (By.XPATH, self.GET_EBOOK_BUTTON).click()
