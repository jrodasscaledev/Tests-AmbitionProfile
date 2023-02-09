import time

from selenium.webdriver import Keys
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
        # COMPANY STRUCTURE TAB
        self.driver.execute_script('arguments[0].click()',
                                   self.driver.find_element(By.XPATH, '/html/body/app-root/div/app-client/div[1]/div[2]/div/app-settings/div/div/aside/ul/li[4]/a'))
        print("--COMPANY STRUCTURE TAB")
        # ADD NEW DEPARTMENT
        self.driver.find_element(By.CLASS_NAME, "set_new_department").click()
        self.driver.find_element(By.CLASS_NAME, "set_new_department").send_keys("Department Test")
        self.driver.find_element(By.CLASS_NAME, "set_new_department").send_keys(Keys.RETURN)
        time.sleep(8)
        # MORE THAN ONE DEPARTMENT ADDED - VALIDATION
        department_item = self.driver.find_elements(By.CLASS_NAME, "department_item")
        print(len(department_item))
        assert len(department_item) >= 1
        # EDIT DEPARTMENT STRUCTURE
        self.driver.find_element(By.CLASS_NAME, "editbtn_depstructure").click()
        deletetestitem = self.driver.find_elements(By.CLASS_NAME, "department_item")
        for department_del in deletetestitem:
            depitem = department_del.text
            # print(depitem)
            if depitem == "Department Test":
                department_del.click()
                time.sleep(10)
            else:
                print("ALL Department Structure created are deleted now")
                assert depitem != "Department Test"

        self.driver.find_element(By.CLASS_NAME, "editbtn_depstructure").click()
        time.sleep(5)

        # ADD NEW COMPANY STRUCTURE
        self.driver.find_element(By.CLASS_NAME, "set_new_location").click()
        self.driver.find_element(By.CLASS_NAME, "set_new_location").send_keys("Company Location Test")
        self.driver.find_element(By.CLASS_NAME, "set_new_location").send_keys(Keys.RETURN)
        time.sleep(8)
        # MORE THAN ONE COMPANY - VALIDATION
        compstruc_item = self.driver.find_elements(By.CLASS_NAME, "companyloc_item")
        print(len(compstruc_item))
        assert len(compstruc_item) >= 1
        # EDIT DEPARTMENT STRUCTURE
        self.driver.find_element(By.CLASS_NAME, "editbtn_comploc").click()
        delcompitems = self.driver.find_elements(By.CLASS_NAME, "companyloc_item")
        for company_del in delcompitems:
            companyitem = company_del.text
            if companyitem == "Company Location Test":
                company_del.click()
                time.sleep(10)
            else:
                print("ALL Company Locations created are deleted now")
                assert companyitem != "Company Location Test"

        self.driver.find_element(By.CLASS_NAME, "editbtn_comploc").click()
        time.sleep(5)