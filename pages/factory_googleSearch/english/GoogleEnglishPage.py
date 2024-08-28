from selenium.webdriver.common.by import By
from driverManager.DriverManager import DriverManager


class GoogleEnglishPage(DriverManager):

    _text_box_search = "//textarea[@name='q']"
    _button_search = "//input[@name='btnK']"

    def __init__(self, browser, driver=None):
        super().__init__(browser, driver)

    def go_to_url(self):
        _url = "https://www.google.com"
        self.get_url(_url)

    def get_textBox_search(self):
        return self.get_driver().find_element(By.XPATH, self._text_box_search)

    def _get_button_search(self):
        return self.get_driver().find_element(By.XPATH, self._button_search)

    def enter_inputToSearch(self, phrase):
        self.is_element_displayed(self.get_textBox_search())
        self.get_textBox_search().send_keys(phrase)

    def clickOn_button_search(self):
        self.is_element_displayed(self._get_button_search())
        self._get_button_search().click()
