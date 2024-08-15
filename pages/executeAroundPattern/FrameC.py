from selenium.webdriver.common.by import By

from driverManager.DriverManager import DriverManager


class FrameC(DriverManager):

    _input_first_name = "//input[@name='fn']"
    _input_last_name = "//input[@name='ln']"
    _input_addr_name = "//input[@name='addr']"
    _input_text_area = "//textarea[@id='area']"

    def __init__(self, service, driver=None ):
        super().__init__(service, driver)

    def get_input_first_name(self):
        return self.get_driver().find_element(By.XPATH, self._input_first_name)

    def get_input_last_name(self):
        return self.get_driver().find_element(By.XPATH, self._input_last_name)

    def get_input_addr_name(self):
        return self.get_driver().find_element(By.XPATH, self._input_addr_name)

    def get_input_text_area(self):
        return self.get_driver().find_element(By.XPATH, self._input_text_area)

    def enter_first_name(self, first_name):
        self.get_input_first_name().send_keys(first_name)

    def enter_last_name(self, last_name):
        self.get_input_last_name().send_keys(last_name)

    def enter_addr_name(self, addr):
        self.get_input_addr_name().send_keys(addr)

    def enter_text_area(self, text):
        self.get_input_text_area().send_keys(text)
