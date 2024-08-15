from pages.paymentProxyPage.components.UserInformation import UserInformation
from pages.paymentProxyPage.components.OrderComponentProxy import OrderComponentProxy
from pages.paymentProxyPage.components.PaymentOption import PaymentOption
from driverManager.DriverManager import DriverManager


class PaymentPage(DriverManager):

    def __init__(self, browser):
        super().__init__(browser, driver=None)
        self.user_information = UserInformation('', self.get_driver())
        self.orderNumber = OrderComponentProxy('', self.get_driver())
        self.paymentOption = PaymentOption

    def go_to_payment_page(self):
        payment_page = "https://vins-udemy.s3.amazonaws.com/ds/strategy.html"
        self.get_url(payment_page)

    def set_user_information(self, first_name, last_name, email):
        self.user_information.enter_user_information(first_name, last_name, email)

    def set_payment_option(self, payment_option):
        self.is_element_displayed(self.user_information.get_input_first_name())
        self.paymentOption = payment_option('', self.get_driver())

    def pay(self, payment_details):
        self.paymentOption.set_payment_information(payment_details)

    def get_order(self):
        return self.orderNumber.placeOrder()
