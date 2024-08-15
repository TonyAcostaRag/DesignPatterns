from selenium.webdriver.common.by import By
from driverManager.DriverManager import DriverManager


class NavigationBar(DriverManager):

    _navigation_Bar = "//div[@class='PHj8of']"
    _button_News = "//div[@role='list']//div[5]//a"
    _button_Tools = "//div[@id='hdtb-tls']"

    def __init__(self, driver=None):
        super().__init__(service=None, driver=driver)

    def get_navigation_Bar(self):
        return self.get_driver().find_element(By.XPATH, self._navigation_Bar)

    def get_button_News(self):
        return self.get_driver().find_element(By.XPATH, self._button_News)

    def clickOn_buttonNews(self):
        self.get_button_News().click()

    def get_button_tools(self):
        return self.get_driver().find_element(By.XPATH, self._button_Tools)

    def clickOn_button_Tools(self):
        self.get_button_tools().click()
