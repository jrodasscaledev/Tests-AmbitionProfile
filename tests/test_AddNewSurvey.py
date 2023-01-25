import time
import pytest
from selenium.webdriver.common.by import By

from TestData.LoginPageData import LoginPageData
from pageObjects.LoginPage import LoginPageProcess
from utilities.BaseClass import BaseClass


class TestAddNewSurvey(BaseClass):
    def test_addnewsurvey(self):
        self.LoginProcessMethod()
        # PRINT IN CONSOLE INFO ABOUT THE WEBSITE
        self.driver.find_element(By.ID, 'create_new_survey').click()
        print("TEST CREATION PAGE")
        print(self.driver.current_url)
        # GO TO CANDIDATE
        self.driver.find_element(By.CLASS_NAME, "candidatebtn_survey").click()
        print("TEST CREATION - STEP ONE - CANDIDATE")
        print(self.driver.current_url)

        # FILL DATA - 3RD STEP
        # FILL TEST NAME FIELD
        self.driver.find_element(By.CLASS_NAME, "namesurvey").send_keys("Test")
        print("NAME FILLED")
        # CLICK ON ALL DEPARTMENTS OPTION
        self.driver.find_element(By.XPATH,
                                 "/html/body/app-root/div/app-client/div[1]/div[2]/div/app-test-creation-wizard/div/div/div[2]/app-test-creation-wizard-second/div/div[4]/label").click()
        # CLICK NEXT ON 3RD STEP
        self.driver.find_element(By.CLASS_NAME, "nextbtn_survey").click()
        print("DATA FILLED")
        # CLICK SEND INVITATIONS LATER
        self.driver.find_element(By.CLASS_NAME, "sendlater_surveybtn").click()
        print("INVITATIONS WILL BE SENT LATER")
        # CLICK SEND SURVEY
        self.driver.find_element(By.CLASS_NAME, "sendsurvey_btn").click()
        print("SURVEY SENT")
        # CLICK "GO TO SURVEY" BUTTON
        self.driver.find_element(By.CLASS_NAME, "gotosurvey_btn").click()

        time.sleep(5)
        print("PROCESS END")








