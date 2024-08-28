from pages.strategy_paymentPage.components.UserInformation import UserInformation
from pages.strategy_paymentPage.components.Order import Order
from pages.strategy_paymentPage.components.PaymentOption import PaymentOption
from driverManager.DriverManager import DriverManager


class PaymentPage(DriverManager):

    def __init__(self, browser):
        super().__init__(browser, driver=None)
        self.user_information = UserInformation('', self.get_driver())
        self.orderNumber = Order('', self.get_driver())
        self.paymentOption = PaymentOption

    def go_to_payment_page(self):
        payment_page = "https://vins-udemy.s3.amazonaws.com/ds/strategy.html"
        self.get_url(payment_page)

    def set_user_information(self, first_name, last_name, email):
        self.user_information.enter_user_information(first_name, last_name, email)

    def get_order(self):
        self.orderNumber.clickOn_Button_Buy()
        return self.orderNumber.get_order_number()

    def set_payment_option(self, payment_option):
        self.is_element_displayed(self.user_information.get_input_first_name())
        self.paymentOption = payment_option('', self.get_driver())

    def pay(self, payment_details):
        self.paymentOption.set_payment_information(payment_details)
