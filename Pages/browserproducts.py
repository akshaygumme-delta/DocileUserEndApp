from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
class BrowseCart:
    @staticmethod
    def test_add_to_cart (appium_driver):
        ele_press_browse_products = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Browse Products"]'
                 ))
        )
        ele_press_browse_products.click()
        ele_add_new_products = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="addCartFav74"]/android.widget.ImageView'
                 ))
        )
        ele_add_new_products.click()
        ele_add_prod_ok = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="OK"]'
                 ))
        )
        ele_add_prod_ok.click()
        ele_click_cart_image = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH,
                 '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ImageView')
            )
        )
        ele_click_cart_image.click()
        ele_change_address = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH,
                 '//android.widget.TextView[@text="Change"]')
            )
        )
        ele_change_address.click()
        ele_change_location_pointer = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH,
                 '//android.view.View[@content-desc="Google Map"]/android.view.View]')
            )
        )
        ele_change_location_pointer.send_keys("Your Desired Location")
        ele_change_location_pointer.send_keys(Keys.RETURN)

        ele_conf_continue = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH,
                 '//android.widget.TextView[@text="Confirm & Continue"]')
            )
        )
        ele_conf_continue.click()

