from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DynamicLoadingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._dynamic_loading_link = (By.LINK_TEXT, "Dynamic Loading")
        self._example2_link = (By.LINK_TEXT, "Example 2: Element rendered after the fact")
        self._start_button = (By.CSS_SELECTOR, "#start button")
        self._loading_message = (By.CSS_SELECTOR, "#finish h4")

    def go_to_dynamic_loading(self):
        self.wait_for_clickable(self._dynamic_loading_link).click()

    def select_example2(self):
        self.wait_for_clickable(self._example2_link).click()

    def click_start(self):
        self.wait_for_clickable(self._start_button).click()

    def get_loading_message(self):
        return self.wait_for_visible(self._loading_message).text