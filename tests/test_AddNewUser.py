import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.BaseClass import BaseClass
class TestAddUsersSetting(BaseClass):
    def test_settingsaddusers(self):
        self.LoginProcessMethod()
        self.driver.find_element(By.CLASS_NAME, 'settings-header').click()
        # USERS PAGE
        self.driver.find_element(By.XPATH, "/html/body/app-root/div/app-client/div[1]/div[2]/div/app-settings/div/div/aside/ul/li[1]/a").click()
        v_usersstgs = self.driver.find_element(By.CLASS_NAME, "useremail_row").text
        if v_usersstgs == "":
            raise Exception("No Users in database or Email text missed")
        print("--Users Page--")
        self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.CSS_SELECTOR, "div[class='btn-newuser'] button[class='button primary ng-star-inserted']"))
        time.sleep(5)
        print("buttontst")
