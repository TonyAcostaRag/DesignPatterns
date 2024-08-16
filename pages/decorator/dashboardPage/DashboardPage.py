from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from driverManager.DriverManager import DriverManager


class DashboardPage(DriverManager):

    _dropdown_role = "//select[@id='role']"
    _list_guest = "//div[@class='hello guest']"
    _list_admin = "//div[@class='hello admin']"
    _list_superuser = "//div[@class='hello superuser']"

    def __init__(self, service, driver=None):
        super().__init__(service, driver)

    def go_to_dashboard_page(self):
        _url = "https://vins-udemy.s3.amazonaws.com/ds/decorator.html"
        self.get_url(_url)

    def _get_dropdown_role(self):
        return Select(self.get_driver().find_element(By.XPATH, self._dropdown_role))

    def selectRole(self, value):
        self._get_dropdown_role().select_by_value(value)

    def get_list_guest(self):
        return self.get_driver().find_elements(By.XPATH, self._list_guest)

    def get_list_admin(self):
        return self.get_driver().find_elements(By.XPATH, self._list_admin)

    def get_list_superuser(self):
        return self.get_driver().find_elements(By.XPATH, self._list_superuser)
