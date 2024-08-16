class PaymentPromoDecorators:
    def __init__(self, paymentPromoPage):
        self._paymentPromoPage = paymentPromoPage

    def apply_free_coupon(self):
        self._paymentPromoPage.enter_promo_code('FREEUDEMY')
        self._paymentPromoPage.click_on_Apply_Button()
        return self

    def apply_discount_coupon(self):
        self._paymentPromoPage.enter_promo_code('PARTIALUDEMY')
        self._paymentPromoPage.click_on_Apply_Button()
        return self

    def use_valid_cc(self):
        self._paymentPromoPage.enter_cc_num('4111111111111111')
        self._paymentPromoPage.enter_cc_year('2023')
        self._paymentPromoPage.enter_cc_cvv('123')
        return self

    def use_invalid_cc(self):
        self._paymentPromoPage.enter_cc_num('4111111111111112')
        self._paymentPromoPage.enter_cc_year('2022')
        self._paymentPromoPage.enter_cc_cvv('222')
        return self

    def buy(self):
        self._paymentPromoPage.click_on_Buy_Button()
        return self._paymentPromoPage.get_total_cost()


    def is_passed_transaction_status(self):
        return self._paymentPromoPage.get_status_code() == 'PASS'

    def free_coupon(self):
        return self.apply_free_coupon().buy()

    def partial_coupon(self):
        return self.apply_discount_coupon().use_valid_cc().buy()

    def valid_cc(self):
        return self.use_valid_cc().buy()

    def invalid_cc(self):
        return self.use_invalid_cc().buy()

    def invalid_cc_partial_coupon(self):
        return self.use_invalid_cc().apply_discount_coupon().buy()

    def get_payment_option(self, option):
        payment_methods = {
            'free_coupon': self.free_coupon,
            'partial_coupon': self.partial_coupon,
            'valid_cc': self.valid_cc,
            'invalid_cc': self.invalid_cc,
            'invalid_cc_partial_coupon': self.invalid_cc_partial_coupon,
            'buy': self.buy
        }
        return payment_methods[option]()
