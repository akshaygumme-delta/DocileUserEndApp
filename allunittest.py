import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from Pages import getstarted,signup,signin,forgotpassword,browserproducts,addtocart,enteraddress
from selenium.webdriver.common.keys import Keys
import main
@pytest.fixture(scope="module")
def appium_driver():
    options = AppiumOptions()
    options.load_capabilities({
            "platformName": "Android",
            "deviceName": "adb-10BD9D2K350007X-mczaYj._adb-tls-connect._tcp",

        })
    # Add other desired capabilities as needed

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    yield driver
    # driver.quit()


@pytest.mark.usefixtures("appium_driver")
class Testunittestcases:
    @staticmethod
    def test_register_user_tc001(appium_driver):
        main.TestAppiumAutomation.test_click_docile_element(appium_driver)
        getstarted.start.test_click_get_started_element(appium_driver)
        ele_signup_home_click = WebDriverWait(appium_driver, 20).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="Sign up"]'
                     ))
            )
        ele_signup_home_click.click()
        signup.SignupPage.fill_signup_details(appium_driver)
        signin.SigninPage.test_enter_signin_info(appium_driver)
        main.TestAppiumAutomation.test_close_app(appium_driver)
