import time
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass

# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        self.LoginProcessMethod()
        log.info("Getting Data")

        print(self.driver.current_url)
        loginsuccesful = self.driver.find_element(By.CLASS_NAME, "hometitle").text
        assert ("Meet our Personas" in loginsuccesful)