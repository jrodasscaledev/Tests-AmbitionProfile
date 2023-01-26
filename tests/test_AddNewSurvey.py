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
        time.sleep(8)
        # ASSERT IF DONT PASS TO THE CREATION TEST PAGE
        creation_page = self.driver.find_element(By.CLASS_NAME, "test_creation_title").text
        assert ("Who will you test?" in creation_page)

        # GO TO CANDIDATE
        self.driver.find_element(By.CLASS_NAME, "candidatebtn_survey").click()
        print("TEST CREATION - STEP ONE - CANDIDATE")
        print(self.driver.current_url)
        # ASSERT IF DONT PASS TO THE CANDIDATE OPTION
        candidate_page = self.driver.find_element(By.CLASS_NAME, "surveyinfo_title").text
        assert ("Survey Information" in candidate_page)

        # FILL DATA - 3RD STEP
        # FILL TEST NAME FIELD
        self.driver.find_element(By.CLASS_NAME, "namesurvey").send_keys("Test")
        print("NAME FILLED")
        # ASSERT IF CANDIDATE SURVEY NAME IS EMPTY
        candidatename_page = self.driver.find_element(By.CLASS_NAME, "namesurvey").text
        assert ("" in candidatename_page)

        # CLICK ON ALL DEPARTMENTS OPTION
        self.driver.find_element(By.XPATH,
                                 "/html/body/app-root/div/app-client/div[1]/div[2]/div/app-test-creation-wizard/div/div/div[2]/app-test-creation-wizard-second/div/div[4]/label").click()
        # CLICK NEXT ON 3RD STEP
        self.driver.find_element(By.CLASS_NAME, "nextbtn_survey").click()
        print("DATA FILLED")
        # ASSERT IF DATA IS NOT FILLED AND DONT PASS TO INVITE PEOPLE PAGE
        surveydatafilled = self.driver.find_element(By.CLASS_NAME, "test-creation-wizard-third__respondants").text
        assert ("Invite People" in surveydatafilled)
        # CLICK SEND INVITATIONS LATER
        self.driver.find_element(By.CLASS_NAME, "sendlater_surveybtn").click()
        print("INVITATIONS WILL BE SENT LATER")
        #ASSERT IF DONT PASS TO "REVIEW AND SEND" PAGE
        surveyreviewpage = self.driver.find_element(By.CLASS_NAME, "test-creation-wizard-fourth").text
        assert ("Review and Send" in surveyreviewpage)
        # CLICK SEND SURVEY
        self.driver.find_element(By.CLASS_NAME, "sendsurvey_btn").click()
        print("SURVEY SENT")
        # ASSERT IF CANDIDATE SURVEY NAME IS EMPTY
        surveysent = self.driver.find_element(By.CLASS_NAME, "test-creation-wizard-fifth__message").text
        assert ("Great, Your survey is sent!" in surveysent)
        # CLICK "GO TO SURVEY" BUTTON
        self.driver.find_element(By.CLASS_NAME, "gotosurvey_btn").click()
        time.sleep(5)
        print("PROCESS END")
        surveyprocessend = self.driver.find_element(By.CLASS_NAME, "survey-detail__header__facts").text
        assert ("Survey settings" in surveyprocessend)









