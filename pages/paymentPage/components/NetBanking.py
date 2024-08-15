from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.paymentPage.components.PaymentOption import PaymentOption


class NetBanking(PaymentOption):

    _dropdown_bank = "//select[@id='bank']"
    _input_account = "//input[@id='acc_number']"
    _input_pin = "//input[@id='pin']"

    def __init__(self, service, driver=None):
        super().__init__(service, driver)

    def _get_dropdown_bank(self):
        return self.get_driver().find_element(By.XPATH, self._dropdown_bank)

    def _get_input_account(self):
        return self.get_driver().find_element(By.XPATH, self._input_account)

    def _get_input_pin(self):
        return self.get_driver().find_element(By.XPATH, self._input_pin)

    def enter_account(self, account):
        self._get_input_account().send_keys(account)

    def enter_pin(self, pin):
        self._get_input_pin().send_keys(pin)

    def enter_payment_details(self, payment_details):
        select = Select(self._get_dropdown_bank())
        select.select_by_value(payment_details['bank'])
        self.enter_account(payment_details['account'])
        self.enter_pin(payment_details['pin'])
