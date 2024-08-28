from pages.factory_googleSearch.english.GoogleEnglishPage import GoogleEnglishPage
from pages.factory_googleSearch.french.GoogleFrenchPage import GoogleFrenchPage
from pages.factory_googleSearch.arabic.GoogleArabicPage import GoogleArabicPage
from pages.factory_googleSearch.spanish.GoogleSpanishPage import GoogleSpanishPage
from pages.factory_googleSearch.english.GoogleEnglishResultPage import GoogleEnglishResultPage
from pages.factory_googleSearch.french.GoogleFrenchResultPage import GoogleFrenchResultPage
from pages.factory_googleSearch.arabic.GoogleArabicResultPage import GoogleArabicResultPage
from pages.factory_googleSearch.spanish.GoogleSpanishResultPage import GoogleSpanishResultPage


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
