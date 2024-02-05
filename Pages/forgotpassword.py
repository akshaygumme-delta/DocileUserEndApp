import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Forgotpassword:
    @staticmethod
    def test_forgot_password(appium_driver):
        ele_for_pass = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Forgot Password?"]'
                 ))
        )
        ele_for_pass.click()
        ele_enter_mob_no = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Enter your Phone Number"]')
        ))
        ele_enter_mob_no.send_keys('6301518207')

        ele_send_btn = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Send"]')
        ))
        ele_send_btn.click()


        ele_enter_pass = WebDriverWait(appium_driver,20).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Enter Password"]'))
        )
        ele_enter_pass.send_keys('Akshay12')

        ele_confirm_pass = WebDriverWait(appium_driver,20).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Confirm Password"]'))
        )
        ele_enter_pass.send_keys('Akshay12')

