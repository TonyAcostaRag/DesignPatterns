from driverManager.DriverManager import DriverManager


class PaymentOption(DriverManager):

    def enter_payment_details(self, payment_details):
        pass

    def set_payment_information(self, payment_details):
        self.enter_payment_details(payment_details)
