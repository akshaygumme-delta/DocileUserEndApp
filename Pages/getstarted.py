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
