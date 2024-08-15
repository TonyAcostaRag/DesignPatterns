import time
import pytest
from pages.googleSearch.GoogleFactory import GoogleFactory


class TestGoogleSearch:

    @pytest.mark.parametrize("language, browser, input_search", [
        ("english", "chrome", "selenium webdriver"),
        ("french", "chrome", "selenium webdriver"),
        ("arabic", "chrome", "selenium webdriver"),
        ("spanish", "chrome", "selenium webdriver"),
        ("english", "firefox", "selenium webdriver"),
        ("french", "firefox", "selenium webdriver"),
        ("arabic", "firefox", "selenium webdriver"),
        ("spanish", "firefox", "selenium webdriver")
    ])
    def test_google_search(self, language, browser, input_search):

        google_page = GoogleFactory.get_page(self, language=language, browser=browser)
        google_page.go_to_url()
        assert google_page.is_element_displayed(google_page.get_textBox_search())

        google_page.enter_inputToSearch(input_search)
        google_page.clickOn_button_search()

        google_result = GoogleFactory.get_result_page(self, language=language, browser=browser, driver=google_page.get_driver())
        assert len(google_result.get_results_list()) >= 1

        google_result.quit_driver()
