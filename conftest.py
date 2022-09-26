import time

import pytest as pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome("C:\\Users\\Srinivas\\PycharmProjects\\Assignment1\\Driver\\chromedriver.exe")
    driver.get("https://www.amazon.in/")
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(20)

    time.sleep(10)
    yield
    driver.close()




