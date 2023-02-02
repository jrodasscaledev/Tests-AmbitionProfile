import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass


class TestEditSurvey(BaseClass):
    def test_editsurvey(self):
        self.LoginProcessMethod()
        self.driver.find_element(By.CLASS_NAME, 'allsurveys').click()
        print("ALLSURVEYS")
        self.driver.find_element(By.XPATH, '//*[@id="surv-column"]').click()
        time.sleep(8)
        surveyedit = self.driver.find_element(By.CLASS_NAME, 'survey-detail__header__facts').text
        assert ("Survey settings" in surveyedit)
        print("ONE SURVEY")
        # SELECT ALL CHECKBOXES
        # Show results checkbox
        # self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.ID, 'mat-slide-toggle-1-input'))
        # time.sleep(8)
        # Gender checkbox
        # self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.ID, 'mat-slide-toggle-2-input'))
        # time.sleep(8)
        # Education Level Checkbox
        # self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.ID, 'mat-slide-toggle-3-input'))
        # time.sleep(8)
        # Department Checkbox
        # self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.ID, 'mat-slide-toggle-4-input'))
        # deparmentchbx = self.driver.find_element(By.ID, 'mat-slide-toggle-4-input').get_attribute('aria-checked')
        # assert deparmentchbx == "false"
        # time.sleep(8)

        print("ALL CHECKED")

        # EDIT SURVEY DEADLINE
        # self.driver.find_element(By.CLASS_NAME, 'edit_deadline_survey').click()
        # time.sleep(10)
        # DESELECT ALL CHECKBOXES
        # self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.ID, 'mat-slide-toggle-1-input'))
        # time.sleep(8)
        # self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.ID, 'mat-slide-toggle-2-input'))
        # time.sleep(8)
        # self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.ID, 'mat-slide-toggle-3-input'))
        # time.sleep(8)
        # self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.ID, 'mat-slide-toggle-4-input'))
        # time.sleep(8)
        print("ALL UNCHECKED")

        self.driver.find_element(By.CLASS_NAME, 'edit_deadline_survey').click()
        time.sleep(2)
        self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.CLASS_NAME, 'mat-calendar-next-button'))
        # self.driver.find_element(By.CLASS_NAME, 'mat-calendar-next-button').click()
        # self.driver.find_element(By.XPATH, '//*[@id="mat-datepicker-0"]/mat-calendar-header/div/div/button[3]').click()
        time.sleep(8)
        alldates = self.driver.find_elements(By.CLASS_NAME, "mat-calendar-body-cell-content")
        for dateelement in alldates:
            data = dateelement.text
            if data == "1":
                dateelement.click()
                break
                print(dateelement)

        # EMPTY DEADLINE VALIDATION
        sd_txt = self.driver.find_element(By.CLASS_NAME, 'survey_deadline_txt').text
        assert "" in sd_txt
        print(sd_txt)

        # UNSELECT THE LANGUAGE AND SELECT GERMAN
        dropdown = Select(self.driver.find_element(By.CLASS_NAME, 'select-lng-list'))
        dropdown.select_by_index(0)
        dropdown.select_by_value("DE")
        dropdown.select_by_index(0)
        time.sleep(5)
        dropdown_txt = dropdown.first_selected_option.text
        if dropdown_txt == "German":
            raise Exception("Select Language Error")
        if dropdown_txt == "":
            raise Exception("Select Language is Empty")
        # assert "" in dropdown_txt
        print(dropdown_txt)

        # SHARE SURVEY URL CHECKBOX - BUTTON TESTING
        if self.driver.find_element(By.ID, "mat-slide-toggle-5-input").get_attribute("aria-checked") == "true":
            # print("Element is ALREADY checked")
            self.driver.execute_script('arguments[0].click()',
                                       self.driver.find_element(By.CLASS_NAME, 'sharesurveyurl'))
            time.sleep(5)
            self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.CLASS_NAME, 'qrcodesrvy'))
            time.sleep(5)
        else:
            self.driver.execute_script('arguments[0].click()',
                                       self.driver.find_element(By.ID, 'mat-slide-toggle-5-input'))
            time.sleep(8)
            self.driver.execute_script('arguments[0].click()',
                                       self.driver.find_element(By.CLASS_NAME, 'sharesurveyurl'))
            time.sleep(5)
            self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.CLASS_NAME, 'qrcodesrvy'))
            time.sleep(5)

        # SHARE CHECKBOX VALIDATION
        if self.driver.find_element(By.ID, "mat-slide-toggle-5-input").get_attribute("aria-checked") == "false":
            raise Exception("ERROR: SHARE SURVEY URL CANT BE CLICKED")
    # def test_shareurl(self):

