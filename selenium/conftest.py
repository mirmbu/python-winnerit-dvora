import pytest
from selenium import webdriver
from time import sleep


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox() # in Firefox browser, the window not closed automatically. need the driver.quit()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    # after test
    # driver.quit()
    sleep(1)