import inspect
import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
    def LoginProcessMethod(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[name=login-email]").send_keys("jrodas@scaledev.gt")
        self.driver.find_element(By.CSS_SELECTOR, "input[name=login-pass]").send_keys("jrodas123*")
        self.driver.find_element(By.ID, 'loginbutton').click()
        time.sleep(8)
        self.driver.implicitly_wait(10)

    def saveformsubmit(self):
        self.driver.execute_script('arguments[0].click()', self.driver.find_element(By.CLASS_NAME, 'sbmt-cinfo'))
        time.sleep(8)
        self.driver.refresh()
    # def verifyLinkPresence(self):
        # element = WebDriverWait(self.driver, 10).until(
            # EC.presence_of_element_located(By.LINK_TEXT, "India")
        # )