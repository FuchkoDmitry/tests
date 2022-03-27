from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class YandexAuth:

    def __init__(self, login, password, browser, link):
        self.LOGIN = login
        self.PASSWORD = password
        self.browser = browser
        self.LINK = link

    def authorize(self):
        self.browser.get(self.LINK)

        self.browser.find_element(By.ID, 'passp-field-login').send_keys(self.LOGIN)
        self.browser.find_element(By.CSS_SELECTOR, 'button.Button2').click()
        self.browser.implicitly_wait(3)

        try:
            password_field = self.browser.find_element(By.ID, 'passp-field-passwd')
        except NoSuchElementException:
            return 'Invalid login'
        password_field.send_keys(self.PASSWORD)
        self.browser.find_element(By.ID, 'passp:sign-in').click()
        time.sleep(3)
        try:
            self.browser.find_element(By.ID, 'passp-field-passwd')
            return 'Invalid password'
        except NoSuchElementException:
            return True
