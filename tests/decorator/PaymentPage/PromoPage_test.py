import pytest
from pages.decorator.paymentPage.PaymentPromoPage import PaymentPromoPage
from pages.decorator.paymentPage.PaymentPromoDecorators import PaymentPromoDecorators


class TestPaymentPromoPage:

    @pytest.mark.parametrize("browser, payment_option, expected_cost, expected_status", [
        ('chrome', 'free_coupon', '0', True),
        ('chrome', 'partial_coupon', '299', True),
        ('chrome', 'valid_cc', '999', True),
        ('chrome', 'invalid_cc', '999', False),
        ('chrome', 'invalid_cc_partial_coupon', '299', False),
        ('chrome', 'buy', '999', False),
        ('firefox', 'free_coupon', '0', True),
        ('firefox', 'partial_coupon', '299', True),
        ('firefox', 'valid_cc', '999', True),
        ('firefox', 'invalid_cc', '999', False),
        ('firefox', 'invalid_cc_partial_coupon', '299', False),
        ('firefox', 'buy', '999', False)
    ])
    def test_free_coupon(self, browser, payment_option, expected_cost, expected_status):
        promo_page = PaymentPromoPage(browser)
        promo_page.go_to_promo_page()
        dec = PaymentPromoDecorators(promo_page)

        assert dec.get_payment_option(payment_option) == expected_cost
        assert dec.is_passed_transaction_status() == expected_status
        promo_page.quit_driver()
