from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class CartPage:
    @staticmethod
    def test_cart_add_remove_item(appium_driver):
        ele_press_browse_products = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Browse Products"]'
                 ))
        )
        ele_press_browse_products.click()
        ele_click_dishwash = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Dishwash Cleaner"]'))
        )
        ele_click_dishwash.click()

