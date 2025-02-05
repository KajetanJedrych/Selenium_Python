from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class DragAndDropPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._drag_drop_link = (By.LINK_TEXT, "Drag and Drop")
        self._column_a = (By.ID, "column-a")
        self._column_b = (By.ID, "column-b")

    def go_to_drag_and_drop(self):
        self.wait_for_clickable(self._drag_drop_link).click()

    def drag_element_a_to_b(self):
        source = self.wait_for_visible(self._column_a)
        target = self.wait_for_visible(self._column_b)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def get_column_a_text(self):
        return self.wait_for_visible(self._column_a).text

    def get_column_b_text(self):
        return self.wait_for_visible(self._column_b).text