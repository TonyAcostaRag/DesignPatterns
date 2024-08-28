from selenium.webdriver.common.by import By
from driverManager.DriverManager import DriverManager


class ResultStats(DriverManager):

    _label_result_text = "//div[@id='result-stats']"

    def __init__(self, driver=None):
        super().__init__(service=None, driver=driver)

    def get_result_text(self):
        return self.get_driver().find_element(By.XPATH, self._label_result_text).text
