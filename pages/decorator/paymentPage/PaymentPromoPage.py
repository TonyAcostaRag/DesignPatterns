from selenium.webdriver.common.by import By
from driverManager.DriverManager import DriverManager


class PaymentPromoPage(DriverManager):

    _input_promo = "//input[@id='coupon']"
    _button_apply = "//input[@id='couponbtn']"
    _input_cc = "//input[@id='cc']"
    _input_year = "//input[@id='year']"
    _input_cvv = "//input[@id='cvv']"
    _label_total = "//td[@id='price']"
    _button_buyNow = "//input[@id='buy']"
    _label_status = "//td[@id='status']"

    def __init__(self, browser, driver=None):
        super().__init__(browser, driver)

    def go_to_promo_page(self):
        _url = "https://vins-udemy.s3.amazonaws.com/java/html/java8-payment-screen.html"
        self.get_url(_url)

    def enter_promo_code(self, code):
        self.get_driver().find_element(By.XPATH, self._input_promo).send_keys(code)

    def click_on_Apply_Button(self):
        self.get_driver().find_element(By.XPATH, self._button_apply).click()

    def enter_cc_num(self, cc_num):
        self.get_driver().find_element(By.XPATH, self._input_cc).send_keys(cc_num)

    def enter_cc_year(self, cc_year):
        self.get_driver().find_element(By.XPATH, self._input_year).send_keys(cc_year)

    def enter_cc_cvv(self, cc_cvv):
        self.get_driver().find_element(By.XPATH, self._input_cvv).send_keys(cc_cvv)

    def get_total_cost(self):
        return self.get_driver().find_element(By.XPATH, self._label_total).text

    def click_on_Buy_Button(self):
        self.get_driver().find_element(By.XPATH, self._button_buyNow).click()

    def get_status_code(self):
        return self.get_driver().find_element(By.XPATH, self._label_status).text
