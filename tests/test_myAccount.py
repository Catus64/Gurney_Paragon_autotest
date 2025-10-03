import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utils.initial_state_skip import initial_state_skip
from pages.navbar_view import navbar_view
from pages.login_page_view import login_page_view
import time
import logging


logging.basicConfig(level=logging.INFO)

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Samsung',
    appPackage='com.convep.gurneyparagon',
    appActivity='com.convep.gurneyparagon.MainActivity',
    language='en',
    locale='US',
    noReset=False,
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_login(self) -> None:

        initial_state_skip(self.driver,"android")
        nav = navbar_view(self.driver,"android")
        nav.navigate("myAccount")
        loginPage = login_page_view(self.driver,"android")
        time.sleep(5)
        loginPage.login()

if __name__ == '__main__':
    unittest.main()