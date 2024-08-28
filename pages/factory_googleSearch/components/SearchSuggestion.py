from selenium.webdriver.common.by import By
from driverManager.DriverManager import DriverManager


class SearchSuggestion(DriverManager):

    _firstPart_nResult_option = "//li["
    _secondPart_nResult_option = "]//div[@class='eIPGRd']//div[@class='pcTkSc']"

    def __init__(self, driver=None):
        super().__init__(service=None, driver=driver)

    def clickOn_suggestionByIndex(self, n):
        full_nResult_option = self._firstPart_nResult_option + str(n) + self._secondPart_nResult_option
        self.get_driver().find_element(By.XPATH, full_nResult_option).click()
