import time
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
class TestAccountSettings(BaseClass):
    def test_accountsettings(self):
        self.LoginProcessMethod()
        self.driver.find_element(By.CLASS_NAME, 'settings-header').click()
        # SETTINGS PAGE VALIDATION
        clientsettings = self.driver.find_element(By.CLASS_NAME, 'settings__menu').text
        assert ("Settings" in clientsettings)
        print("---Settings Page---")
        # ACCOUNT SETTINGS TAB
        self.driver.execute_script('arguments[0].click()',
                                   self.driver.find_element(By.XPATH, '/html/body/app-root/div/app-client/div[1]/div[2]/div/app-settings/div/div/aside/ul/li[3]/a'))
        print("--ACCOUNT SETTINGS TAB")
        time.sleep(8)
        # ACCOUNT INFO VALIDATION
        accountsettings = self.driver.find_element(By.CLASS_NAME, "fn_AccountSettings").text
        assert ("First name:" == accountsettings)
        # FIRST NAME FIELD - CLEAR, FILL, SAVE
        self.driver.find_element(By.CLASS_NAME, 'fn_AccountSettings_in').clear()
        self.driver.find_element(By.CLASS_NAME, 'fn_AccountSettings_in').send_keys("First Name ScaleDev")
        firstname_accsett_ant = self.driver.find_element(By.CLASS_NAME, 'fn_AccountSettings_in').get_attribute('value')
        self.saveformsubmit()
        self.driver.refresh()
        self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.XPATH,
                                                                                    '/html/body/app-root/div/app-client/div[1]/div[2]/div/app-settings/div/div/aside/ul/li[3]/a'))
        time.sleep(8)
        firstname_accsett = self.driver.find_element(By.CLASS_NAME, 'fn_AccountSettings_in').get_attribute('value')
        assert firstname_accsett_ant == firstname_accsett

        # LAST NAME FIELD - CLEAR, FILL, SAVE
        self.driver.find_element(By.CLASS_NAME, 'fn_LNSettings_in').clear()
        self.driver.find_element(By.CLASS_NAME, 'fn_LNSettings_in').send_keys("Last Name ScaleDev")
        lname_accsett_ant = self.driver.find_element(By.CLASS_NAME, 'fn_LNSettings_in').get_attribute('value')
        self.saveformsubmit()
        self.driver.refresh()
        self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.XPATH,
                                                                                    '/html/body/app-root/div/app-client/div[1]/div[2]/div/app-settings/div/div/aside/ul/li[3]/a'))
        time.sleep(8)
        lname_accsett = self.driver.find_element(By.CLASS_NAME, 'fn_LNSettings_in').get_attribute('value')
        assert lname_accsett_ant == lname_accsett
        print(lname_accsett)

        # EMAIL FIELD - CLEAR, FILL, SAVE
        # emailname_accsett = self.driver.find_element(By.CLASS_NAME, 'fn_EmailSettings_in').get_attribute('value')
        # print(emailname_accsett)
        # time.sleep(8)
        # self.driver.find_element(By.CLASS_NAME, 'fn_EmailSettings_in').clear()
        # self.driver.find_element(By.CLASS_NAME, 'fn_EmailSettings_in').send_keys("testemail@scaledev.gt")
        # emailnamechange_accsett = self.driver.find_element(By.CLASS_NAME, 'fn_EmailSettings_in').get_attribute('value')
        # print(emailnamechange_accsett)
        # assert emailname_accsett != emailnamechange_accsett
        # self.driver.find_element(By.CLASS_NAME, 'fn_EmailSettings_in').clear()
        # self.driver.find_element(By.CLASS_NAME, 'fn_EmailSettings_in').send_keys(emailname_accsett)
        # self.saveformsubmit()
        # self.driver.refresh()

        # PHONE FIELD - CLEAR, FILL, SAVE
        self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.XPATH,
                                                                                    '/html/body/app-root/div/app-client/div[1]/div[2]/div/app-settings/div/div/aside/ul/li[3]/a'))
        time.sleep(5)
        as_actualphone = self.driver.find_element(By.CLASS_NAME, 'fn_phone_in').get_attribute('value')
        print(as_actualphone)
        self.driver.find_element(By.CLASS_NAME, 'fn_phone_in').clear()
        self.driver.find_element(By.CLASS_NAME, 'fn_phone_in').send_keys("123456")
        as_changephone = self.driver.find_element(By.CLASS_NAME, 'fn_phone_in').get_attribute('value')
        print(as_changephone)
        assert as_changephone != as_actualphone
        self.driver.find_element(By.CLASS_NAME, 'fn_phone_in').clear()
        self.driver.find_element(By.CLASS_NAME, 'fn_phone_in').send_keys(as_actualphone)
        self.saveformsubmit()
        self.driver.refresh()
        time.sleep(5)