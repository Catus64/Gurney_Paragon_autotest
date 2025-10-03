from .base_page import base_page
from appium.webdriver.common.appiumby import AppiumBy
from utils.helpers import wait_for_element,log_info,wait
from utils.locators import locate_login

class login_page_view(base_page):
    def __init__(self, driver, platform):
        super().__init__(driver, platform)

        self.load_element()
        self.set_auth()

    def load_element(self):
        self.card_num_input = wait_for_element(self.driver,3,AppiumBy.CLASS_NAME, "android.widget.EditText")
        self.pass_input = wait_for_element(self.driver,3,AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.widget.EditText\").instance(1)")
        self.login_button = wait_for_element(self.driver,3,AppiumBy.ACCESSIBILITY_ID,"LOG IN")

    def platform_setup(self):
        return super().platform_setup()
    
    def set_auth(self):
        log = locate_login()
        self.username = log["username"]
        self.password = log["password"]
        


    def login(self):
        log_info(f"Logging in with {self.username}, {self.password}")
        self.card_num_input.send_keys(self.username)
        self.pass_input.send_keys(self.password)
        self.login_button.click()
        wait(5)
        pass
