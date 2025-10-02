import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import logging

class initial_promo_view():
    def __init__(self,driver,platform):
        logging.info(f"{__name__} initializing initial promo view class")

        self.is_exist = True


        self.driver = driver
        if platform == "android":
            logging.info("loaded initial promo page on android")
        elif platform == "ios":
            logging.info("loaded initial promo page on android")
        
        wait = WebDriverWait(self.driver,5)

        try:
            self.skip_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, " SKIP "))
            )
            yes_button = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=" Yes ")
        except TimeoutException:
            self.is_exist = False
        logging.info(f"{__name__} Elements are loaded")

    def skip_promo(self):
        logging.info(f"{initial_promo_view.skip_promo.__qualname__} Pressing Skip Button \n")
        self.skip_button.click()
    
    def yes_promo(self):
        pass

