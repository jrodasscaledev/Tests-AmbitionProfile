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
        self.saveformsubmit()
        v_compnameant = self.driver.find_element(By.CLASS_NAME, 'companyname-stgs').get_attribute('value')
        self.driver.refresh()
        v_compname = self.driver.find_element(By.CLASS_NAME, 'companyname-stgs').get_attribute('value')
        assert v_compnameant == v_compname
        # INDUSTRY
        self.driver.find_element(By.CLASS_NAME, 'industry-stgs').clear()
        self.driver.find_element(By.CLASS_NAME, 'industry-stgs').send_keys("Marketing Test")
        self.saveformsubmit()
        v_industryant = self.driver.find_element(By.CLASS_NAME, 'industry-stgs').get_attribute('value')
        self.driver.refresh()
        v_industry = self.driver.find_element(By.CLASS_NAME, 'industry-stgs').get_attribute('value')
        print(v_industryant)
        assert v_industryant == v_industry
        # v_industry = self.driver.find_element(By.CLASS_NAME, 'industry-stgs').get_attribute('value')
        # print(v_industry)
        # assert "" in v_industry
        # ADDRESS
        self.driver.find_element(By.CLASS_NAME, 'address-stgs').clear()
        self.driver.find_element(By.CLASS_NAME, 'address-stgs').send_keys("Scaledev Guatemala Test")
        self.saveformsubmit()
        v_addressant = self.driver.find_element(By.CLASS_NAME, 'address-stgs').get_attribute('value')
        self.driver.refresh()
        v_address = self.driver.find_element(By.CLASS_NAME, 'address-stgs').get_attribute('value')
        print(v_addressant)
        assert v_addressant == v_address
        # POSTAL CODE
        self.driver.find_element(By.CLASS_NAME, 'pc-stgs').clear()
        self.driver.find_element(By.CLASS_NAME, 'pc-stgs').send_keys("01010")
        self.saveformsubmit()
        v_postalcodeant = self.driver.find_element(By.CLASS_NAME, 'pc-stgs').get_attribute('value')
        self.driver.refresh()
        v_postalcode = self.driver.find_element(By.CLASS_NAME, 'pc-stgs').get_attribute('value')
        print(v_postalcodeant)
        assert v_postalcodeant == v_postalcode
        # CITY
        self.driver.find_element(By.CLASS_NAME, 'city-stgs').clear()
        self.driver.find_element(By.CLASS_NAME, 'city-stgs').send_keys("Guatemala test")
        self.saveformsubmit()
        v_cityant = self.driver.find_element(By.CLASS_NAME, 'city-stgs').get_attribute('value')
        self.driver.refresh()
        v_city = self.driver.find_element(By.CLASS_NAME, 'city-stgs').get_attribute('value')
        print(v_cityant)
        assert v_cityant == v_city
        # COUNTRY
        self.driver.find_element(By.CLASS_NAME, 'country-stgs').clear()
        self.driver.find_element(By.CLASS_NAME, 'country-stgs').send_keys("Guatemala test")
        self.saveformsubmit()
        v_countryant = self.driver.find_element(By.CLASS_NAME, 'country-stgs').get_attribute('value')
        self.driver.refresh()
        v_country = self.driver.find_element(By.CLASS_NAME, 'country-stgs').get_attribute('value')
        print(v_countryant)
        assert v_countryant == v_country
        # VAT NUMBER
        self.driver.find_element(By.CLASS_NAME, 'vatno-stgs').clear()
        self.driver.find_element(By.CLASS_NAME, 'vatno-stgs').send_keys("123456789")
        self.saveformsubmit()
        v_vatnoant = self.driver.find_element(By.CLASS_NAME, 'vatno-stgs').get_attribute('value')
        self.driver.refresh()
        v_vatno = self.driver.find_element(By.CLASS_NAME, 'vatno-stgs').get_attribute('value')
        print(v_vatnoant)
        assert v_vatnoant == v_vatno
        # NUMBER OF EMPLOYEES
        self.driver.find_element(By.CLASS_NAME, 'noemp-stgs').clear()
        self.driver.find_element(By.CLASS_NAME, 'noemp-stgs').send_keys("2")
        self.saveformsubmit()
        v_noempant = self.driver.find_element(By.CLASS_NAME, 'noemp-stgs').get_attribute('value')
        self.driver.refresh()
        v_noemp = self.driver.find_element(By.CLASS_NAME, 'noemp-stgs').get_attribute('value')
        print(v_noempant)
        assert v_noempant == v_noemp
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

        self.saveformsubmit()
        print("All settings changed")
