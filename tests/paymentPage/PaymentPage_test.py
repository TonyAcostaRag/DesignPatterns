import time
import pytest
from pages.paymentPage.PaymentPage import PaymentPage
from pages.paymentPage.components.CreditCard import CreditCard
from pages.paymentPage.components.NetBanking import NetBanking
from pages.paymentPage.components.PayPal import PayPal


class TestPaymentPage:

    @pytest.mark.parametrize("browser, firstname, lastname, email, payment_option, payment_details", [
        ("chrome", "Tony", "Acosta", "tony@email", CreditCard, {'cc_num': '12341234', 'cc_year': '2030', 'cc_cvv': '333'}),
        ("chrome", "Tony", "Acosta", "tony@email", NetBanking, {'bank': 'BOFA', 'account': '333333', 'pin': '1234'}),
        ("chrome", "Tony", "Acosta", "tony@email", PayPal, {'paypal_username': 'username', 'paypal_password': 'password'}),
        ("firefox", "Tony", "Acosta", "tony@email", CreditCard, {'cc_num': '12341234', 'cc_year':'2030', 'cc_cvv': '333'}),
        ("firefox", "Tony", "Acosta", "tony@email", NetBanking, {'bank': 'BOFA', 'account': '333333', 'pin': '1234'}),
        ("firefox", "Tony", "Acosta", "tony@email", PayPal, {'paypal_username': 'username', 'paypal_password': 'password'}),
    ])
    def test_payment_option(self, browser, firstname, lastname, email, payment_option, payment_details):

        payment_page = PaymentPage(browser)

        payment_page.go_to_payment_page()
        payment_page.set_user_information(firstname, lastname, email)
        payment_page.set_payment_option(payment_option)
        payment_page.pay(payment_details)
        order_number = payment_page.get_order()

        print('\nOrder number:', order_number)

        time.sleep(1)
        payment_page.quit_driver()
