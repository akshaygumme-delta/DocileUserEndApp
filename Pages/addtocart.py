from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Addtocart:
    @staticmethod
    def test_add_product(appium_driver):
        ele_click_mixture = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Baby Oil"]'))
        )
        ele_click_mixture.click()
        ele_click_mixture = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Baby Soap"]'))
        )
        # appium_driver.scroll(ele_click_mixture)
        ele_click_mixture.click()
        ele_add_btn = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.TextView[@text="Add"])[1]'))
        )
        ele_add_btn.click()
        ele_ok_btn = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.TextView[@text="OK"])'))
        )
        ele_ok_btn.click()
        ele_back_btn = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="goBackBtn"]/android.widget.ImageView '))
        )
        ele_back_btn.click()
        ele_click_cart = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.ImageView'))
        )
        ele_click_cart.click()
        ele_continue_click = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="CONTINUE"]'))
        )
        ele_continue_click.click()