from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from pages.base_page import BasePage

class JavaScriptAlertsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._js_alerts_link = (By.LINK_TEXT, "JavaScript Alerts")
        self._js_alert_button = (By.XPATH, "//button[contains(text(), 'Click for JS Alert')]")
        self._js_confirm_button = (By.XPATH, "//button[contains(text(), 'Click for JS Confirm')]")
        self._js_prompt_button = (By.XPATH, "//button[contains(text(), 'Click for JS Prompt')]")
        self._result = (By.ID, "result")

    def go_to_javascript_alerts(self):
        self.wait_for_clickable(self._js_alerts_link).click()

    def trigger_alert(self):
        self.wait_for_clickable(self._js_alert_button).click()
        Alert(self.driver).accept()

    def trigger_confirm(self):
        self.wait_for_clickable(self._js_confirm_button).click()
        Alert(self.driver).accept()

    def trigger_prompt(self, text):
        self.wait_for_clickable(self._js_prompt_button).click()
        alert = Alert(self.driver)
        alert.send_keys(text)
        alert.accept()

    def get_result_text(self):
        return self.wait_for_visible(self._result).text