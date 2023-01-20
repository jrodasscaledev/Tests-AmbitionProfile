import time

import pytest
from selenium.webdriver.common.by import By


class LoginPageProcess:
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.CSS_SELECTOR, "input[name=login-email]").send_keys("jrodas@scaledev.gt")
    email = (By.CSS_SELECTOR, "input[name=login-email]")
    # self.driver.find_element(By.CSS_SELECTOR, "input[name=login-pass]").send_keys("jrodas123*")
    loginpass = (By.CSS_SELECTOR, "input[name=login-pass]")
    # self.driver.find_element(By.ID, 'loginbutton').click()
    submit = (By.ID, 'loginbutton')

    # DEFINE METHODS TO BE CALLED IN test_LoginTests.py
    def getEmail(self):
        return self.driver.find_element(*LoginPageProcess.email)

    def getPass(self):
        return self.driver.find_element(*LoginPageProcess.loginpass)

    def LoginSubmit(self):
        return self.driver.find_element(*LoginPageProcess.submit)


