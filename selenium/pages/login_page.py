from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, browser):
        self.browser = browser



    def open_home_page(self):
        self.browser.get("https://www.saucedemo.com/")

    def type_user_name(self, username):
        user_name_input_field = self.browser.find_element(By.ID, "user-name")  # [id="user-name"] | #user-name
        user_name_input_field.clear()
        user_name_input_field.send_keys(username)

    def type_password(self, password):
        password_input_field = self.browser.find_element(By.CSS_SELECTOR, '[data-test="password"]')
        password_input_field.clear()
        password_input_field.send_keys(password)

    def click_login_button(self):
        self.browser.find_element(By.NAME, "login-button").click()