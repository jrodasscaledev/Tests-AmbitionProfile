import time
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        self.LoginProcessMethod()
        log.info("Getting Data")

        print(self.driver.current_url)
