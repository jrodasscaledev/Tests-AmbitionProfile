import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.BaseClass import BaseClass
class TestEditSurvey(BaseClass):
    def test_clientsettings(self):
        self.LoginProcessMethod()
        self.driver.find_element(By.CLASS_NAME, 'settings-header').click()
        # SETTINGS PAGE VALIDATION
        clientsettings = self.driver.find_element(By.CLASS_NAME, 'settings__menu').text
        assert ("Settings" in clientsettings)
        print("---Settings Page---")
        # COMPANY NAME
        self.driver.find_element(By.CLASS_NAME, 'companyname-stgs').clear()
        self.driver.find_element(By.CLASS_NAME, 'companyname-stgs').send_keys("Test ScaleDev")
        self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.CLASS_NAME, 'sbmt-cinfo'))
        time.sleep(8)
        v_compname = self.driver.find_element(By.CLASS_NAME, 'companyname-stgs').get_attribute('value')
        assert "" in v_compname
        self.driver.refresh()
        print(v_compname)
        # INDUSTRY
        self.driver.find_element(By.CLASS_NAME, 'industry-stgs').clear()
        self.driver.find_element(By.CLASS_NAME, 'industry-stgs').send_keys("Marketing Test")
        v_industry = self.driver.find_element(By.CLASS_NAME, 'industry-stgs').text
        assert "" in v_industry
        # ADDRESS
        self.driver.find_element(By.CLASS_NAME, 'address-stgs').clear()
        self.driver.find_element(By.CLASS_NAME, 'address-stgs').send_keys("Scaledev Guatemala Test")
        v_address = self.driver.find_element(By.CLASS_NAME, 'address-stgs').text
        assert "" in v_address
        # POSTAL CODE
        self.driver.find_element(By.CLASS_NAME, 'pc-stgs').clear()
        self.driver.find_element(By.CLASS_NAME, 'pc-stgs').send_keys("01010")
        v_postalcode = self.driver.find_element(By.CLASS_NAME, 'pc-stgs').text
        assert "" in v_postalcode
        # CITY
        self.driver.find_element(By.CLASS_NAME, 'city-stgs').clear()
        self.driver.find_element(By.CLASS_NAME, 'city-stgs').send_keys("Guatemala test")
        v_postalcode = self.driver.find_element(By.CLASS_NAME, 'city-stgs').text
        assert "" in v_postalcode
        # COUNTRY
        self.driver.find_element(By.CLASS_NAME, 'country-stgs').clear()
        self.driver.find_element(By.CLASS_NAME, 'country-stgs').send_keys("Guatemala test")
        v_country = self.driver.find_element(By.CLASS_NAME, 'country-stgs').text
        assert "" in v_country
        # VAT NUMBER
        self.driver.find_element(By.CLASS_NAME, 'vatno-stgs').clear()
        self.driver.find_element(By.CLASS_NAME, 'vatno-stgs').send_keys("123456789")
        v_vatno = self.driver.find_element(By.CLASS_NAME, 'vatno-stgs').text
        assert "" in v_vatno
        # NUMBER OF EMPLOYEES
        self.driver.find_element(By.CLASS_NAME, 'noemp-stgs').clear()
        self.driver.find_element(By.CLASS_NAME, 'noemp-stgs').send_keys("2")
        v_vatno = self.driver.find_element(By.CLASS_NAME, 'noemp-stgs').text
        assert "" in v_vatno
        # SELECT PREFERRED LANGUAGE
        dropdown = Select(self.driver.find_element(By.CLASS_NAME, 'lang-stgs'))
        ENlang = dropdown.select_by_value("EN")
        SElang = dropdown.select_by_value("SE")
        if ENlang:
            dropdown.select_by_value("SE")
        if SElang:
            dropdown.select_by_value("EN")
        dropdown_txt = dropdown.first_selected_option.text
        if dropdown_txt == "":
            raise Exception("Select Language is Empty")
        # time.sleep(5)

        self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.CLASS_NAME, 'sbmt-cinfo'))
        time.sleep(10)
        print("All settings changed")
