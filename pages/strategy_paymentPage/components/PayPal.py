from pages.strategy_paymentPage.components.PaymentOption import PaymentOption
from selenium.webdriver.common.by import By


class PayPal(PaymentOption):

    _input_username = "//input[@id='paypal_username']"
    _input_password = "//input[@id='paypal_password']"

    def __init__(self, service, driver=None):
        super().__init__(service, driver)

    def _get_input_username(self):
        return self.get_driver().find_element(By.XPATH, self._input_username)

    def _get_input_password(self):
        return self.get_driver().find_element(By.XPATH, self._input_password)

    def enter_username(self, username):
        self._get_input_username().send_keys(username)

    def enter_password(self, password):
        self._get_input_password().send_keys(password)

    def enter_payment_details(self, payment_details):
        self.enter_username(payment_details['paypal_username'])
        self.enter_password(payment_details['paypal_password'])
