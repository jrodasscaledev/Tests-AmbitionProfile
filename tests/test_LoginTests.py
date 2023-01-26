import time

import pytest
from selenium.webdriver.common.by import By

from TestData.LoginPageData import LoginPageData
from pageObjects.LoginPage import LoginPageProcess
from utilities.BaseClass import BaseClass


class TestLogin(BaseClass):
    def test_loginsubmission(self, getData):
        log = self.getLogger()
        loginpage = LoginPageProcess(self.driver)
        loginpage.getEmail().send_keys(getData["Email"])
        # log.info("Reading Email")
        loginpage.getPass().send_keys(getData["Pass"])
        log.info("Reading Password")
        self.driver.find_element(By.ID, 'loginbutton').click()
        log.info("Submit Login Process")
        # time.sleep(10)
        print(self.driver.current_url)
        self.driver.refresh()
        loginunsuccesful = self.driver.find_element(By.CLASS_NAME, "loginh1title").text
        assert ("Welcome Back" in loginunsuccesful)

    def test_loginsubmitsuccess(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[name=login-email]").send_keys("jrodas@scaledev.gt")
        self.driver.find_element(By.CSS_SELECTOR, "input[name=login-pass]").send_keys("jrodas123*")
        self.driver.find_element(By.ID, 'loginbutton').click()
        loginsuccesful = self.driver.find_element(By.CLASS_NAME, "hometitle").text
        assert ("Meet our Personas" in loginsuccesful)


    @pytest.fixture(params=LoginPageData.test_LoginPage_Data)
    def getData(self, request):
        return request.param