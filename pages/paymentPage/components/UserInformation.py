from driverManager.DriverManager import DriverManager
from selenium.webdriver.common.by import By


class UserInformation(DriverManager):

    _input_first_name = "//input[@id='fn']"
    _input_last_name = "//input[@id='ln']"
    _input_email = "//input[@id='email']"

    def __init__(self, browser, driver=None):
        super().__init__(browser, driver)

    def get_input_first_name(self):
        return self.get_driver().find_element(By.XPATH, self._input_first_name)

    def get_input_last_name(self):
        return self.get_driver().find_element(By.XPATH, self._input_last_name)

    def get_input_email(self):
        return self.get_driver().find_element(By.XPATH, self._input_email)

    def enter_first_name(self, first_name):
        self.get_input_first_name().send_keys(first_name)

    def enter_last_name(self, last_name):
        self.get_input_last_name().send_keys(last_name)

    def enter_email(self, email):
        self.get_input_email().send_keys(email)

    def enter_user_information(self, first_name, last_name, email):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
