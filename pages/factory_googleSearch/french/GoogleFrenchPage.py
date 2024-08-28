from selenium.webdriver.common.by import By
from pages.factory_googleSearch.english.GoogleEnglishPage import GoogleEnglishPage


class GoogleFrenchPage(GoogleEnglishPage):

    _button_francais = "//a[text()='Français']"

    def __init__(self, service, driver=None):
        super().__init__(service, driver)

    def go_to_url(self):
        _url = "https://www.google.fr"
        self.get_url(_url)

    def _get_button_francais(self):
        return self.get_driver().find_element(By.XPATH, self._button_francais)

    def clickOn_button_francais(self):
        self._get_button_francais().click()

    def enter_inputToSearch(self, phrase):
        self.clickOn_button_francais()
        super().enter_inputToSearch(phrase)
