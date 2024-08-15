from pages.googleSearch.english.GoogleEnglishResultPage import GoogleEnglishResultPage


class GoogleFrenchResultPage(GoogleEnglishResultPage):
    def __init__(self, service, driver=None):
        super().__init__(service, driver)
