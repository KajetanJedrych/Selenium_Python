from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._username_input = (By.ID, "username")
        self._password_input = (By.ID, "password")
        self._login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self._success_message = (By.CSS_SELECTOR, "div.flash.success")
        self._error_message = (By.CSS_SELECTOR, "div.flash.error")

    def login(self, username, password):
        self.wait_for_element(self._username_input).send_keys(username)
        self.wait_for_element(self._password_input).send_keys(password)
        self.wait_for_element(self._login_button).click()

    def get_success_message(self):
        return self.wait_for_visible(self._success_message).text

    def get_error_message(self):
        return self.wait_for_visible(self._error_message).text
