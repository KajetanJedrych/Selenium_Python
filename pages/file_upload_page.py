from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FileUploadPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._file_upload_link = (By.LINK_TEXT, "File Upload")
        self._file_input = (By.ID, "file-upload")
        self._upload_button = (By.ID, "file-submit")
        self._upload_message = (By.TAG_NAME, "h3")

    def go_to_file_upload(self):
        self.wait_for_clickable(self._file_upload_link).click()

    def upload_file(self, file_path):
        self.wait_for_element(self._file_input).send_keys(file_path)
        self.wait_for_element(self._upload_button).click()

    def get_upload_message(self):
        return self.wait_for_visible(self._upload_message).text