from datetime import time
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("C:/Users/Javier Rodas/Documents/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    # elif browser_name == "firefox":
        # service_obj = Service("C:/Users/Javier Rodas/Documents/geckodriver.exe")
        # driver = webdriver.Firefox(service=service_obj)

    # Chrome Options -- Headless Mode
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("headless")
    # -- Chrome
    # service_obj = Service("C:/Users/Javier Rodas/Documents/chromedriver.exe")
    # driver = webdriver.Chrome(service=service_obj)
    # driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    # driver.implicitly_wait(5)
    # -- Firefox
    # service_obj= Service("C:/Users/Javier Rodas/Documents/geckodriver.exe")
    # driver = webdriver.Firefox(service=service_obj)

    # FULLWITH WINDOW
    # driver.maximize_window()
    # LOGIN FUNCTION
    # driver.get("http://localhost:4200/")
    # driver.find_element(By.CSS_SELECTOR, "input[name=login-email]").send_keys("jrodas@scaledev.gt")
    # driver.find_element(By.CSS_SELECTOR, "input[name=login-pass]").send_keys("jrodas123*")
    # REDIRECT TO DASHBOARD
    # driver.execute_script('arguments[0].click()', driver.find_element(By.ID, 'loginbutton'))
    # driver.find_element(By.ID, 'loginbutton').click()
    # time.sleep(10)
    # print(driver.current_url)
    # driver.get("https://app.ambitionprofile.com/")
    driver.get("http://localhost:4200")
    driver.maximize_window()



    request.cls.driver = driver
    yield
    driver.close()
