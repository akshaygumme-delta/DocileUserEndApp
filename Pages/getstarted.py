from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class start:
    @staticmethod
    def test_click_get_started_element(appium_driver):
        ele_get_started = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Get Started"]'))
        )
        ele_get_started.click()
        # ele_change_location = WebDriverWait(appium_driver, 20).until(
        #     EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Hyderabad"]'))
        # )
        # ele_change_location.click()
        # ele_new_address = WebDriverWait(appium_driver, 20).until(
        #     EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Search a new address"]'))
        # )
        # ele_new_address.send_keys('siddipet')
        # ele_new_address_click = WebDriverWait(appium_driver, 20).until(
        #     EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Siddipet, Telangana, India"]'))
        # )
        # ele_new_address_click.click()
        # ele_conf_continue_click= WebDriverWait(appium_driver, 20).until(
        #     EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Confirm & Continue"]'))
        # )
        # ele_conf_continue_click.click()
