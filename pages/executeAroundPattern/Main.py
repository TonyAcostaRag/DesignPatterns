from selenium.webdriver.common.by import By
from driverManager.DriverManager import DriverManager
from pages.executeAroundPattern.FrameA import FrameA
from pages.executeAroundPattern.FrameB import FrameB
from pages.executeAroundPattern.FrameC import FrameC


class Main(DriverManager):

    _frame_a = "//frame[@id='a']"
    _frame_b = "//frame[@id='b']"
    _frame_c = "//frame[@id='c']"

    def __init__(self, service, driver=None):
        self.frame_a = FrameA
        self.frame_b = FrameB
        self.frame_c = FrameC
        super().__init__(service, driver)

    def call_frame_action(self, frame, action, text):
        frame_methods = {
            'enter_first_name': frame.enter_first_name,
            'enter_last_name': frame.enter_last_name,
            'enter_address': frame.enter_addr_name,
            'enter_text_area': frame.enter_text_area
        }

        frame_methods[action](text)

    def go_to_Main_page(self):
        _url = "https://vins-udemy.s3.amazonaws.com/ds/main.html"
        self.get_url(_url)

    def get_frame_a(self):
        self.get_driver().switch_to.default_content()
        self.get_driver().switch_to.frame(self.get_driver().find_element(By.XPATH, self._frame_a))
        return self.frame_a('', self.get_driver())

    def get_frame_b(self):
        self.get_driver().switch_to.default_content()
        self.get_driver().switch_to.frame(self.get_driver().find_element(By.XPATH, self._frame_b))
        return self.frame_b('', self.get_driver())

    def get_frame_c(self):
        self.get_driver().switch_to.default_content()
        self.get_driver().switch_to.frame(self.get_driver().find_element(By.XPATH, self._frame_c))
        return self.frame_c('', self.get_driver())

    def perform_OnFrameA(self, action, text):
        # 1. ir al frame A (pre-action)
        frame = self.get_frame_a()

        # 2. Hacer la accion en el frame A
        self.call_frame_action(frame, action, text)

        # 3. Regresar al default content (post-action)
        self.get_driver().switch_to.default_content()

    def perform_OnFrameB(self, action, text):
        # 1. ir al frame (pre-action)
        frame = self.get_frame_b()

        # 2. Hacer la accion en el frame
        self.call_frame_action(frame, action, text)

        # 3. Regresar al default content (post-action)
        self.get_driver().switch_to.default_content()

    def perform_OnFrameC(self, action, text):
        # 1. ir al frame A (pre-action)
        frame = self.get_frame_c()

        # 2. Hacer la accion en el frame A
        self.call_frame_action(frame, action, text)

        # 3. Regresar al default content (post-action)
        self.get_driver().switch_to.default_content()

