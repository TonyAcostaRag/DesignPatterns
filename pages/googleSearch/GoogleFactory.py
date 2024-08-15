from pages.googleSearch.english.GoogleEnglishPage import GoogleEnglishPage
from pages.googleSearch.french.GoogleFrenchPage import GoogleFrenchPage
from pages.googleSearch.arabic.GoogleArabicPage import GoogleArabicPage
from pages.googleSearch.spanish.GoogleSpanishPage import GoogleSpanishPage

from pages.googleSearch.english.GoogleEnglishResultPage import GoogleEnglishResultPage
from pages.googleSearch.french.GoogleFrenchResultPage import GoogleFrenchResultPage
from pages.googleSearch.arabic.GoogleArabicResultPage import GoogleArabicResultPage
from pages.googleSearch.spanish.GoogleSpanishResultPage import GoogleSpanishResultPage


class GoogleFactory:

    def get_page(self, language, browser, driver=None):

        pageLanguage_factory = {
            'english': GoogleEnglishPage,
            'french': GoogleFrenchPage,
            'arabic': GoogleArabicPage,
            'spanish': GoogleSpanishPage
        }

        return pageLanguage_factory[language](browser, driver)

    def get_result_page(self, language, browser, driver=None):

        pageResult_factory = {
            'english': GoogleEnglishResultPage,
            'french': GoogleFrenchResultPage,
            'arabic': GoogleArabicResultPage,
            'spanish': GoogleSpanishResultPage
        }

        return pageResult_factory[language](browser, driver)
