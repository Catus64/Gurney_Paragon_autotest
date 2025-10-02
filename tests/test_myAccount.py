import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.initial_promo_view import initial_promo_view
from utils.initial_state_skip import initial_state_skip
import time
import logging

logging.basicConfig(level=logging.INFO)

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Huawei',
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
        #time.sleep(5)

if __name__ == '__main__':
    unittest.main()