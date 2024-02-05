import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SigninPage:
    @staticmethod
    def test_enter_signin_info(appium_driver):
        ele_mobile_no = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Phone Number"]'))
        )

        # Clear any existing text in the input field (optional)
        ele_mobile_no.clear()

        # Enter the mobile number into the input field
        ele_mobile_no.send_keys('6301518207')  # Change the phone number as needed

        # Assert that the entered text in the input field matches the expected value
        assert ele_mobile_no.text == '6301518207', "Failed to enter the correct phone number"

        ele_sign_in_continue = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Continue"]'))
        )
        ele_sign_in_continue.click()

        time.sleep(20)

        ele_next = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Next"]'))
        )

        ele_next.click()
        ele_change_location = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Hyderabad"]'))
        )
        ele_change_location.click()
        ele_new_address = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Search a new address"]'))
        )
        ele_new_address.send_keys('siddipet')
        ele_new_address_click = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Siddipet, Telangana, India"]'))
        )
        ele_new_address_click.click()
        ele_conf_continue_click = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Confirm & Continue"]'))
        )
        ele_conf_continue_click.click()
    @staticmethod
    def test_sign_with_password(appium_driver):
        ele_mobile_no = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Phone Number"]'))
        )

        # Clear any existing text in the input field (optional)
        ele_mobile_no.clear()

        # Enter the mobile number into the input field
        ele_mobile_no.send_keys('6301518207')

        ele_password_enter = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Password"]'))
        )
        ele_password_enter.clear()
        ele_password_enter.send_keys('Ravi@1234')
        ele_login_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Login"]'
                                        ))
        )
        ele_login_button.click()

