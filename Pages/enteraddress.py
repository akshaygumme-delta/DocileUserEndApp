from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Address:
    @staticmethod
    def test_enter_address (appium_driver):
        ele_enter_complete_add = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Enter complete address"]'
        ))
        )
        ele_enter_complete_add.click()
        ele_enter_house_no = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@text="House No. & Floor *"]'
        ))
        )
        ele_enter_house_no.send_keys('203')
        ele_enter_building_name = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@text="Building & Block No *"]'
        ))
        )
        ele_enter_building_name.send_keys('Delta IoT')
        ele_save_btn = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Save"]'
        ))
        )
        ele_save_btn.click()
        ele_continue_address = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Continue"]'
        ))
        )
        ele_continue_address.click()
        ele_continue_order = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="CONTINUE"]'
                 ))
        )
        ele_continue_order.click()
        ele_order_now_click = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Order Now"]'
                 ))
        )
        ele_order_now_click.click()
        ele_track_order = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Track Order"]'
                 ))
        )
        ele_track_order.click()