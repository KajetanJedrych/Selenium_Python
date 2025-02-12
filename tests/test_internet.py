import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from pages.login_page import LoginPage
from pages.dynamic_loading_page import DynamicLoadingPage
from pages.file_upload_page import FileUploadPage
from pages.javascript_alerts_page import JavaScriptAlertsPage
from pages.drag_and_drop_page import DragAndDropPage
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService



@pytest.fixture
def driver(request):
    if request.param == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif request.param == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    
    driver.maximize_window()
    yield driver
    driver.quit()

class TestInternet:
    BASE_URL = "https://the-internet.herokuapp.com"

    def test_login_with_valid_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate_to(f"{self.BASE_URL}/login")
        login_page.login("tomsmith", "SuperSecretPassword!")
        assert "You logged into a secure area!" in login_page.get_success_message()

    def test_login_with_invalid_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate_to(f"{self.BASE_URL}/login")
        login_page.login("invalidUser", "invalidPassword")
        assert "Your username is invalid!" in login_page.get_error_message()

    def test_dynamic_loading(self, driver):
        dynamic_page = DynamicLoadingPage(driver)
        dynamic_page.navigate_to(self.BASE_URL)
        dynamic_page.go_to_dynamic_loading()
        dynamic_page.select_example2()
        dynamic_page.click_start()
        assert dynamic_page.get_loading_message() == "Hello World!"

    def test_file_upload(self, driver):
        file_page = FileUploadPage(driver)
        file_page.navigate_to(self.BASE_URL)
        file_page.go_to_file_upload()
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../sampleFile.txt"))
        file_page.upload_file(file_path)
        assert "File Upl" in file_page.get_upload_message()

    def test_javascript_alerts(self, driver):
        alerts_page = JavaScriptAlertsPage(driver)
        alerts_page.navigate_to(self.BASE_URL)
        alerts_page.go_to_javascript_alerts()
        
        alerts_page.trigger_alert()
        assert "You successfully clicked an alert" in alerts_page.get_result_text()
        
        alerts_page.trigger_confirm()
        assert "You clicked: Ok" in alerts_page.get_result_text()
        
        prompt_text = "I am a JS Confirm"
        alerts_page.trigger_prompt(prompt_text)
        assert f"You entered: {prompt_text}" in alerts_page.get_result_text()

    def test_drag_and_drop(self, driver):
        drag_drop_page = DragAndDropPage(driver)
        drag_drop_page.navigate_to(self.BASE_URL)
        drag_drop_page.go_to_drag_and_drop()
        
        initial_a_text = drag_drop_page.get_column_a_text()
        initial_b_text = drag_drop_page.get_column_b_text()
        
        drag_drop_page.drag_element_a_to_b()
        
        assert drag_drop_page.get_column_a_text() == initial_b_text
        assert drag_drop_page.get_column_b_text() == initial_a_text