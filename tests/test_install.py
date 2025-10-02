import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Redmi 10 5G',
    appPackage='com.convep.gurneyparagon',
    appActivity='com.convep.gurneyparagon.MainActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_apps(self) -> None:
        wait = WebDriverWait(self.driver,15)
        accept_button = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, " Yes "))
        )
        accept_button.click()    
        #time.sleep(5)
        #el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=" Yes ")
        #el1.click()
        #el2 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(19)")
        #el2.click()
        #time.sleep(5)

if __name__ == '__main__':
    unittest.main()