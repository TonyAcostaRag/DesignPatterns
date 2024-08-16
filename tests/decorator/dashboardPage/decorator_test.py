import time
import pytest
from pages.decorator.dashboardPage.DashboardPage import DashboardPage
from pages.decorator.dashboardPage.Decorators import Decorators


class TestDecorator:

    @pytest.mark.parametrize("browser, role", [
        ("chrome", "guest"),
        ('chrome', "superuser"),
        ('chrome', "admin"),
        ('firefox', "guest"),
        ('firefox', "superuser"),
        ('firefox', "admin")
    ])
    def test_decorator(self, browser, role):

        dashboardPage = DashboardPage(browser)
        dashboardPage.go_to_dashboard_page()
        dec = Decorators(dashboardPage)

        assert dec.get_validation_role(role) == True
        time.sleep(2)
        dashboardPage.quit_driver()
