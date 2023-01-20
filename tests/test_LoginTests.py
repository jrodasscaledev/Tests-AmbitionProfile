import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from TestData.LoginPageData import LoginPageData
from pageObjects.LoginPage import LoginPageProcess
from utilities.BaseClass import BaseClass


class TestLogin(BaseClass):
    def test_loginsubmission(self, getData):
        log = self.getLogger()
        loginpage = LoginPageProcess(self.driver)
        loginpage.getEmail().send_keys(getData["Email"])
        log.info("Reading Email")
        loginpage.getPass().send_keys(getData["Pass"])
        log.info("Reading Password")
        # self.driver.find_element(*LoginPageProcess.getEmail()).send_keys(getData[0])
        # self.driver.find_element(*LoginPageProcess.getPass()).send_keys(getData[1])
        self.driver.find_element(By.ID, 'loginbutton').click()
        log.info("Submit Login Process")
        time.sleep(5)
        print(self.driver.current_url)
        self.driver.refresh()

    @pytest.fixture(params=LoginPageData.test_LoginPage_Data)
    def getData(self, request):
        return request.param