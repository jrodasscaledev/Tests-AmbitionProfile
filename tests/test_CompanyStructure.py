import time
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
class TestCompanyStructure(BaseClass):
    def test_companystructure(self):
        self.LoginProcessMethod()
        self.driver.find_element(By.CLASS_NAME, 'settings-header').click()
        # SETTINGS PAGE VALIDATION
        clientsettings = self.driver.find_element(By.CLASS_NAME, 'settings__menu').text
        assert ("Settings" in clientsettings)
        print("---Settings Page---")
        # ACCOUNT SETTINGS TAB
        self.driver.execute_script('arguments[0].click()',
                                   self.driver.find_element(By.XPATH, '/html/body/app-root/div/app-client/div[1]/div[2]/div/app-settings/div/div/aside/ul/li[4]/a'))
        print("--COMPANY STRUCTURE TAB")
        time.sleep(8)