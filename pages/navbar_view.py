from appium.webdriver.common.appiumby import AppiumBy
from .base_page import base_page
from utils.helpers import log_info,wait_for_element,find_element,wait

class navbar_view(base_page):
    def __init__(self, driver, platform):
        super().__init__(driver, platform)
        
        self.options_dict = {
            "Home" : None,
            "myAccount" : None,
            "promotion" : None,
            "directory" : None,
            "more" : None,
        }

        self.load_element()
    
    def load_element(self):
        #el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="HOME")
        #el2.click()
        #el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="PROMOTION")
        #el3.click()
        #el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="MY ACCOUNT")
        #el4.click()
        #el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="DIRECTORY")
        #el5.click()
        #el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="MORE")
        #el6.click()
        log_info("start nav")
        self.options_dict["Home"] = wait_for_element(self.driver,2,AppiumBy.ACCESSIBILITY_ID,"HOME")
        self.options_dict["promotion"] = find_element(self.driver,AppiumBy.ACCESSIBILITY_ID,"PROMOTION")
        self.options_dict["myAccount"] = find_element(self.driver,AppiumBy.ACCESSIBILITY_ID,"MY ACCOUNT")
        self.options_dict["directory"] = find_element(self.driver,AppiumBy.ACCESSIBILITY_ID,"DIRECTORY")
        self.options_dict["more"] = find_element(self.driver,AppiumBy.ACCESSIBILITY_ID,"MORE")
        self.is_loaded = True
        log_info("end nav")
        log_info(f"{__name__} Elements are loaded")
    
    def platform_setup(self):
        pass

    def navigate(self,string):
        if(self.options_dict[string]):
            log_info(f"Pressing {string}")
            self.options_dict[string].click()
            return
        raise Exception("args is not part of the nav options")
            