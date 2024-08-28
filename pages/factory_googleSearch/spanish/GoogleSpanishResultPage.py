from pages.factory_googleSearch.english.GoogleEnglishResultPage import GoogleEnglishResultPage


class GoogleSpanishResultPage(GoogleEnglishResultPage):
    def __init__(self, service, driver=None):
        super().__init__(service, driver)
