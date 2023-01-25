from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class TestNewSurvey(BaseClass):
    def test_newsurvey(self):
        self.LoginProcessMethod()
        # PRINT IN CONSOLE INFO ABOUT THE WEBSITE
        self.driver.find_element(By.ID, 'create_new_survey').click()
        print("TEST CREATION PAGE")
        print(self.driver.current_url)
        # GO TO CANDIDATE
        self.driver.find_element(By.CLASS_NAME, "candidatebtn_survey").click()
        print("TEST CREATION - STEP ONE - CANDIDATE")
        print(self.driver.current_url)
        # GO BACK AND GO TO OUR EMPLOYEES
        self.driver.find_element(By.CLASS_NAME, "backbtn_survey").click()
        self.driver.find_element(By.CLASS_NAME, "employeesbtn_survey").click()
        print("TEST CREATION - STEP ONE - OUR EMPLOYEES")
        print(self.driver.current_url)





