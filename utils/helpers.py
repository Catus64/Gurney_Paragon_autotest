from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import logging

def log_info(string):
    logging.info(string)

def wait_for_element(driver,time,by,val,required = False) :
    wait = WebDriverWait(driver,time)
    try:
        button = wait.until(
            EC.element_to_be_clickable((by,val))
        )
        return button
    except TimeoutException:
        if(required):
            raise Exception(f"Elements cannot be found: {by} {val}")
        return None
    
def find_element(driver,byval,val,required = False):
    try:
        button = driver.find_element(by=byval,value = val)
        return button
    except TimeoutException:
        if(required):
            raise Exception(f"Elements cannot be foind: {byval} {val}")
        return None


def wait(length):
    time.sleep(length)