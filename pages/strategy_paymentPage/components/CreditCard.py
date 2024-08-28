from pages.strategy_paymentPage.components.PaymentOption import PaymentOption
from selenium.webdriver.common.by import By


class CreditCard(PaymentOption):

    _input_creditCard_number = "//input[@id='cc']"
    _input_card_year = "//input[@id='year']"
    _input_card_cvv = "//input[@id='cvv']"

    def __init__(self, service, driver=None):
        super().__init__(service, driver)

    def _get_input_creditCard_number(self):
        return self.get_driver().find_element(By.XPATH, self._input_creditCard_number)

    def _get_input_card_year(self):
        return self.get_driver().find_element(By.XPATH, self._input_card_year)

    def _get_input_card_cvv(self):
        return self.get_driver().find_element(By.XPATH, self._input_card_cvv)

    def enter_creditCard_number(self, first_name):
        self._get_input_creditCard_number().send_keys(first_name)

    def enter_card_year(self, last_name):
        self._get_input_card_year().send_keys(last_name)

    def enter_card_ccv(self, email):
        self._get_input_card_cvv().send_keys(email)

    def enter_payment_details(self, payment_details):
        self.enter_creditCard_number(payment_details['cc_num'])
        self.enter_card_year(payment_details['cc_year'])
        self.enter_card_ccv(payment_details['cc_cvv'])
