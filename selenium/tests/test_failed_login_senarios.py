from selenium.webdriver.common.by import By
from pages.login_page import LoginPage



def test_locked_out_user_login(browser):
    # pass the browser to the class to init function.
    login_page = LoginPage(browser)

    # Navigate to the app
    login_page.open_home_page()

    # Filling form
    login_page.type_user_name("locked_out_user")
    login_page.type_password("secret_sauce")
    login_page.click_login_button()

    # Validation of an error message.
    error_message_text = browser.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
    print(f"{error_message_text = }")
    assert error_message_text == "Epic sadface: Sorry, this user has been locked out."
