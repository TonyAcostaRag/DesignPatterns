import time
from selenium.webdriver.common.by import By
from driverManager.DriverManager import DriverManager


class SearchField(DriverManager):

    _textBox_Search = "//textarea[@name='q']"

    def __init__(self, driver=None):
        super().__init__(service=None, driver=driver)

    def get_textBox_Search(self):
        return self.get_driver().find_element(By.XPATH, self._textBox_Search)

    def enter(self, phrase):
        self.get_textBox_Search().clear()
        for char in phrase:
            self.get_textBox_Search().send_keys(char)
            time.sleep(.025)
