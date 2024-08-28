from pages.factory_googleSearch.english.GoogleEnglishResultPage import GoogleEnglishResultPage


class GoogleArabicResultPage(GoogleEnglishResultPage):

    def __init__(self, service, driver):
        super().__init__(service, driver)
