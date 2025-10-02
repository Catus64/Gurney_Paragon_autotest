from .base_page import base_page
from appium.webdriver.common.appiumby import AppiumBy
from utils.helpers import wait_for_element,log_info,wait

class login_page_view(base_page):
    def __init__(self, driver, platform):
        super().__init__(driver, platform)

        self.load_element()

    def load_element(self):
        card_num_icon = wait_for_element(self.driver,3,AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"\").instance(0)")
        pass
    
    def platform_setup(self):
        return super().platform_setup()
