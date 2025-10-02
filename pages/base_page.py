from abc import ABC,abstractmethod
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import logging


class base_page(ABC):
    def __init__(self,driver,platform):
        self.driver = driver
        self.is_loaded = False
        self.platform = platform

    @abstractmethod
    def load_element(self) -> bool:
        """Each page must implent a loading fn for states"""
        pass

    @abstractmethod
    def platform_setup(self):
        """Each page must decide differences for these button elements"""
        pass

