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
        # OPEN MODAL VALIDATION
        v_modaladduser = self.driver.find_element(By.CLASS_NAME, "title_newedituser").text
        if v_modaladduser == "":
            raise Exception("MODAL NOT OPENED")
        print(v_modaladduser)
        # FILL FIELDS ON ADD USER MODAL

        self.driver.find_element(By.CLASS_NAME, 'nameadduser').send_keys("Test Name")
        self.driver.find_element(By.CLASS_NAME, 'emailadduser').send_keys("Test@email.com")
        self.driver.find_element(By.CLASS_NAME, 'dpadduser').send_keys("Test Department")
        self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.CLASS_NAME, "sbmtbtn-usermodal"))
        time.sleep(10)
        # self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.CSS_SELECTOR, "div[class='settings-user-modal__title'] a"))
        # print("buttontst")

        allusers = self.driver.find_elements(By.XPATH, "//body[1]/app-root[1]/div[1]/app-client[1]/div[1]/div[2]/div[1]/app-settings[1]/div[1]/div[1]/div[1]/div[1]/app-settings-users[1]/div[1]/div[2]/table[1]/tbody[1]/tr/td/button[1]")
        i = 0
        for dataelement in allusers:
            self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.CLASS_NAME, "edituserbtn"))
            time.sleep(5)
            self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.CSS_SELECTOR, "div[class='settings-user-modal__title'] a"))
            data = dataelement.text
            assert "" in data
            i += 1
            print(data, i)
