from selenium.webdriver.common.by import By
from pages.login_page import LoginPage



def test_standard_user_login(browser):
    # browser.get("https://www.saucedemo.com/")
    # pass the browser to the class to init the function.
    login_page = LoginPage(browser)

    # Navigate to the app
    login_page.open_home_page()

    # Filling form
    login_page.type_user_name("standard_user")
    login_page.type_password("secret_sauce")
    login_page.click_login_button()


    # Validation of redirection
    current_url = browser.current_url
    print(f"{current_url = }")
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    products_page_title = browser.find_element(By.XPATH, '//*[@data-test="title"]').text
    print(f"{products_page_title = }")
    assert products_page_title == "Products"


