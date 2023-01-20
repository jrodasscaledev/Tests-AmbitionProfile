import time
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        self.LoginProcessMethod()
        log.info("Getting Data")
        # login_page = LoginPage(self.driver)
        # login_page.LoginEmail().send_keys("jrodas@scaledev.gt")
        # login_page.LoginPass().send_keys("jrodas123*")
        # self.driver.find_element(By.CSS_SELECTOR, "input[name=login-email]").send_keys("jrodas@scaledev.gt")
        # self.driver.find_element(By.CSS_SELECTOR, "input[name=login-pass]").send_keys("jrodas123*")
        # REDIRECT TO DASHBOARD
        # self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.ID, 'loginbutton'))
        # self.driver.find_element(By.ID, 'loginbutton').click()
        time.sleep(10)
        print(self.driver.current_url)
