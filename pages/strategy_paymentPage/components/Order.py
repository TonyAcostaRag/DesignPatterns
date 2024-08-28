from selenium.webdriver.common.by import By
from driverManager.DriverManager import DriverManager


class Order(DriverManager):

    _button_buy = "//input[@id='buy']"
    _label_order_numer = "//td[@id='ordernumber']"

    def __init__(self, service, driver=None):
        super().__init__(service, driver)

    def _get_button_buy(self):
        return self.get_driver().find_element(By.XPATH, self._button_buy)

    def _get_label_order_numer(self):
        return self.get_driver().find_element(By.XPATH, self._label_order_numer)

    def clickOn_Button_Buy(self):
        self._get_button_buy().click()

    def get_order_number(self):
        return self._get_label_order_numer().text
