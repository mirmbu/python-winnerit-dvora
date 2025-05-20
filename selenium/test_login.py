import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox() # in Firefox browser, the window not closed automatically. need the driver.quit()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    #after test
    # driver.quit()
    sleep(3)



# def test_basic_login(browser):
#     browser.get("https://www.saucedemo.com/")

def test_standard_user_login(browser):
    browser.get("https://www.saucedemo.com/")

    # Filling form
    user_name_input_field = browser.find_element(By.ID, "user-name") #[id="user-name"] | #user-name
    user_name_input_field.clear()
    user_name_input_field.send_keys("standard_user")
    password_input_field = browser.find_element(By.CSS_SELECTOR, '[data-test="password"]')
    password_input_field.clear()
    password_input_field.send_keys("secret_sauce")
    browser.find_element(By.NAME, "login-button").click()

    # Validation of redirection
    current_url = browser.current_url
    print(f"{current_url = }")
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    products_page_title = browser.find_element(By.XPATH, '//*[@data-test="title"]').text
    print(f"{products_page_title = }")
    assert products_page_title == "Products"




def test_locked_out_user_login(browser):
    browser.get("https://www.saucedemo.com/")

    # Filling form
    user_name_input_field = browser.find_element(By.ID, "user-name")  # [id="user-name"] | #user-name
    user_name_input_field.clear()
    user_name_input_field.send_keys("locked_out_user")
    password_input_field = browser.find_element(By.CSS_SELECTOR, '[data-test="password"]')
    password_input_field.clear()
    password_input_field.send_keys("secret_sauce")
    browser.find_element(By.NAME, "login-button").click()

    # Validation of an error message.
    error_message_text = browser.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
    print(f"{error_message_text = }")
    assert error_message_text == "Epic sadface: Sorry, this user has been locked out."


