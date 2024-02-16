from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException


class AppiumElementFinder:
    def __init__(self, driver):
        self.driver = driver

    def find_clickable_element_by_xpath(self, xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Error finding element by XPath: {xpath}")
            return None

    def find_send_data_by_xpath(self, xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, xpath))
            )
            return element
        except Exception as e:
            print("xpath error")
            return None

    def find_visible_element_by_xpath(self, xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, xpath))
            )
            return element
        except TimeoutException:
            print(f"Element with XPath '{xpath}' not found or not visible within  seconds")
            return None
