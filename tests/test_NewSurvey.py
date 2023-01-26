import time

from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class TestNewSurvey(BaseClass):
    def test_newsurvey(self):
        self.LoginProcessMethod()
        # PRINT IN CONSOLE INFO ABOUT THE WEBSITE
        self.driver.find_element(By.ID, 'create_new_survey').click()
        print("TEST CREATION PAGE")
        print(self.driver.current_url)
        time.sleep(8)
        # ASSERT IF DONT PASS TO THE CREATION TEST PAGE
        createsurvey_page = self.driver.find_element(By.CLASS_NAME, "test_creation_title").text
        assert ("Who will you test?" in createsurvey_page)
        # GO TO CANDIDATE
        self.driver.find_element(By.CLASS_NAME, "candidatebtn_survey").click()
        print("TEST CREATION - STEP ONE - CANDIDATE")
        print(self.driver.current_url)
        # ASSERT IF DONT PASS TO THE CANDIDATE OPTION
        candidate_page = self.driver.find_element(By.CLASS_NAME, "surveyinfo_title").text
        assert ("Survey Information" in candidate_page)
        # GO BACK AND GO TO OUR EMPLOYEES
        self.driver.find_element(By.CLASS_NAME, "backbtn_survey").click()
        self.driver.find_element(By.CLASS_NAME, "employeesbtn_survey").click()
        print("TEST CREATION - STEP ONE - OUR EMPLOYEES")
        ouremployees_page = self.driver.find_element(By.CLASS_NAME, "surveyinfo").text
        assert ("Survey" in ouremployees_page)





