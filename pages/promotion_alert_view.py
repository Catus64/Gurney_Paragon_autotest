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

class promotion_alert_view():


    def __init__(self,driver, type):

        self.driver = driver

        self.wait = WebDriverWait(self.driver,15)

        self.save_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"SAVE\")"))
        )
    
    def save(self):
        self.save_button.click()


        ok_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID," OK "))
        )

        ok_button.click()

        time.sleep(1)