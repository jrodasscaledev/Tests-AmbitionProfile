import time
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
class TestAddUsersSetting(BaseClass):
    def test_settingsEditUser(self):
        self.LoginProcessMethod()
        self.driver.find_element(By.CLASS_NAME, 'settings-header').click()
        # USERS PAGE
        self.driver.find_element(By.XPATH, "/html/body/app-root/div/app-client/div[1]/div[2]/div/app-settings/div/div/aside/ul/li[1]/a").click()
        v_usersstgs = self.driver.find_element(By.CLASS_NAME, "useremail_row").text
        if v_usersstgs == "":
            raise Exception("No Users in database or Email text missed")
        print("--Users Page--")
        time.sleep(8)

        allusers = self.driver.find_elements(By.XPATH, "/html/body/app-root/div/app-client/div[1]/div[2]/div/app-settings/div/div/div/div/app-settings-users/div/div[2]/table/tbody/tr/td/button")
        i = 0
        for dataelement in allusers:
            dataelement.click()
            # self.driver.execute_script('arguments[' + str(i) + '].click()', self.driver.find_element(By.CLASS_NAME, "edituserbtn"))
            time.sleep(5)
            i += 1
            usernameinput = self.driver.find_element(By.CLASS_NAME, "usernamemod").get_attribute('value')
            print(usernameinput, i)
            assert "" != usernameinput
            self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.CLASS_NAME, "closebtn"))
            time.sleep(5)