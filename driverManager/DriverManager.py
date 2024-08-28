from selenium.webdriver.chrome.service import Service as chromeServ
from selenium.webdriver.firefox.service import Service as ffServ
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class DriverManager:

    chromeService = chromeServ(executable_path='drivers/chromedriver')
    firefoxService = ffServ(executable_path='drivers/geckodriver')
    chromeDebug = Options()
    chromeDebug.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    def _get_browser(self, browser):

        browser_dict = {
            'chrome': [webdriver.Chrome, self.chromeService],
            'firefox': [webdriver.Firefox, self.firefoxService]
        }
        return browser_dict[browser][0](service=browser_dict[browser][1])

    def __init__(self, browser, driver=None):
        if driver is None:
            self.__driver = self._get_browser(browser)
            self.__driver.maximize_window()
            self.__driver.implicitly_wait(10)
        else:
            self.__driver = driver

    def get_driver(self):
        return self.__driver

    def quit_driver(self):
        self.__driver.quit()

    def get_url(self, url):
        self.__driver.get(url)

    def _wait_for_element(self):
        wait = WebDriverWait(self.get_driver(), timeout=50, poll_frequency=2)
        return wait

    def is_element_displayed(self, webElement):
        self._wait_for_element().until(ec.visibility_of(webElement))
        return webElement.is_displayed()
