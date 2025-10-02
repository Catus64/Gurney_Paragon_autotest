import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import logging

class initial_promo_view():
    def __init__(self,driver,platform):
        logging.info("initializing initial promo view class")
        self.driver = driver
        if platform == "android":
            logging.info("loaded initial promo page on android")
        elif platform == "ios":
            logging.info("loaded initial promo page on android")
        
        wait = WebDriverWait(self.driver,15)

        #yes_button = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=" Yes ")
        self.skip_button = wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, " SKIP "))
        )

    def __del__():
        logging.info("destroying intial promo view class")

    def skip_promo(self):
        self.skip_button.click()
