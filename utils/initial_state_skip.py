
from pages.initial_promo_view import initial_promo_view
from pages.promotion_alert_view import promotion_alert_view
import logging

def initial_state_skip(driver, phone):
        page1 = initial_promo_view(driver, phone)
        if(page1.is_loaded):
            page1.skip_promo()     
        else:
            logging.info("initial popup is not displayed")
