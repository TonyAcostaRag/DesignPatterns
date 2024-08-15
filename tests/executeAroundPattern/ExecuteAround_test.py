import time
import pytest
from pages.executeAroundPattern.Main import Main


class TestExecuteAround:

    @pytest.mark.parametrize("browser, first_name, last_name, address, text_area", [
        ("chrome", "Tony", "Acosta", "Catarina", "Text_area"),
        ("firefox", "Tony", "Acosta", "Catarina", "Text_area")
    ])
    def test_execute_around(self, browser, first_name, last_name, address, text_area):
        main = Main(browser)
        main.go_to_Main_page()

        main.perform_OnFrameA('enter_first_name', first_name)
        main.perform_OnFrameA('enter_last_name', last_name)
        main.perform_OnFrameA('enter_address', address)
        main.perform_OnFrameA('enter_text_area', text_area)

        main.perform_OnFrameB('enter_first_name', first_name)
        main.perform_OnFrameB('enter_last_name', last_name)
        main.perform_OnFrameB('enter_address', address)
        main.perform_OnFrameB('enter_text_area', text_area)

        main.perform_OnFrameC('enter_first_name', first_name)
        main.perform_OnFrameC('enter_last_name', last_name)
        main.perform_OnFrameC('enter_address', address)
        main.perform_OnFrameC('enter_text_area', text_area)

        time.sleep(2)
        main.quit_driver()
