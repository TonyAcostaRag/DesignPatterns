from selenium.webdriver.common.by import By
from driverManager.DriverManager import DriverManager


class GoogleEnglishResultPage(DriverManager):

    _results_list = "//div[@class='MjjYud']"

    def __init__(self, browser, driver=None):
        super().__init__(browser, driver)

    def get_results_list(self):
        return self.get_driver().find_elements(By.XPATH, self._results_list)
