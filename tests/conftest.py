import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options

driver = None

from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("C\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        service_obj = Service("C:\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj, options=options)
    elif browser_name == "IE":
        print("IE driver")

    # Chrome Options -- Headless Mode
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("headless")

    # driver.get("https://app.ambitionprofile.com/")
    driver.implicitly_wait(10)
    driver.get("http://localhost:4200")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
