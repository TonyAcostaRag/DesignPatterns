from selenium.webdriver.common.by import By
from pages.googleSearch.english.GoogleEnglishPage import GoogleEnglishPage


class GoogleArabicPage(GoogleEnglishPage):

    _button_arabic = "//a[@dir='rtl']"
    _button_keyboard = "//span[@class='ly0Ckb']"
    _keyboard = "//div[@id='kbd']"

    def __init__(self, service, driver=None):
        super().__init__(service, driver)

    def go_to_url(self):
        _url = "https://www.google.com.sa/"
        self.get_url(_url)

    def _get_button_arabic(self):
        return self.get_driver().find_element(By.XPATH, self._button_arabic)

    def _get_button_keyboard(self):
        return self.get_driver().find_element(By.XPATH, self._button_keyboard)

    def clickOn_button_arabic(self):
        self._get_button_arabic().click()

    def clickOn_button_keyboard(self):
        self._get_button_keyboard().click()

    def get_keyboard(self):
        return self.get_driver().find_element(By.XPATH, self._keyboard)

    def enter_inputToSearch(self, phrase):
        self.clickOn_button_arabic()
        self.is_element_displayed(self._get_button_keyboard())
        self.clickOn_button_keyboard()
        self.is_element_displayed(self.get_keyboard())
        super().enter_inputToSearch(phrase)
