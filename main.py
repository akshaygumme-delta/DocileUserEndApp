import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from Pages import getstarted,signup,signin,forgotpassword,browserproducts,addtocart,enteraddress
from selenium.webdriver.common.keys import Keys
@pytest.fixture(scope="module")
def appium_driver():
    options = AppiumOptions()
    options.load_capabilities({
            "platformName": "Android",
            "deviceName": "adb-RZ8R21SMYNN-i8os4l._adb-tls-connect._tcp",

        })
    # Add other desired capabilities as needed

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    yield driver
    # driver.quit()

@pytest.mark.usefixtures("appium_driver")
class TestAppiumAutomation:
    @staticmethod
    def test_click_docile_element(appium_driver):
        el = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Docile"]'
        ))
        )
        el.click()
        WebDriverWait(appium_driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Get Started"]'))
        )
        # # Verification that you're on the next page
        # assert "NextPageActivity" in appium_driver.current_activity

        print("Test Passed! Successfully navigated to the next page.")

    def test_getting_start_element(self, appium_driver):
        getstarted.start.test_click_get_started_element(appium_driver)
        print('Getting Started button successfully clicked')

    def test_add_to_cart(self, appium_driver):
        addtocart.Addtocart.test_add_product(appium_driver)
        print("item added to cart successfully")

    def test_address_and_payment_successful(self, appium_driver):
        enteraddress.Address.test_enter_address(appium_driver)
        print('order placed successfully')

    def test_close_app(self, appium_driver):
        appium_driver.press_keycode(3)
        appium_driver.quit()

    # def test_signin_details(self,appium_driver):
    #     ele_sign_in_click = WebDriverWait(appium_driver, 20).until(
    #         EC.element_to_be_clickable(
    #             (AppiumBy.XPATH, '//android.widget.TextView[@text="Sign in"]'
    #     ))
    #     )
    #     ele_sign_in_click.click()
    #     signin.SigninPage.test_enter_signin_info(appium_driver)

    # def test_forgot_password (self, appium_driver):
    #     ele_sign_in_click = WebDriverWait(appium_driver, 20).until(
    #         EC.element_to_be_clickable(
    #             (AppiumBy.XPATH, '//android.widget.TextView[@text="Sign in"]'
    #              ))
    #     )
    #     ele_sign_in_click.click()
    #     ele_login_with_pass_click = WebDriverWait(appium_driver, 20).until(
    #         EC.element_to_be_clickable(
    #             (AppiumBy.XPATH, '//android.widget.TextView[@text="Login with Password"]'
    #              ))
    #     )
    #     ele_login_with_pass_click.click()
    #     forgotpassword.Forgotpassword.test_forgot_password(appium_driver)
    #
    #
    #
    #
    #
    # def test_dont_hv_account(self, appium_driver):
    #     ele_dont_acc_sign_up = WebDriverWait(appium_driver, 20).until(
    #         EC.element_to_be_clickable(
    #             (AppiumBy.XPATH, '//android.widget.TextView[@text="Don\'t have an account? Sign Up"]'
    #     ))
    #     )
    #     ele_dont_acc_sign_up.click()
    #     signup.SignupPage.fill_signup_details(appium_driver)
    #
    # def test_signup_homepage_click(self, appium_driver):
    #     ele_signup_home_click = WebDriverWait(appium_driver, 20).until(
    #         EC.element_to_be_clickable(
    #             (AppiumBy.XPATH, '//android.widget.TextView[@text="Sign up"]'
    #     ))
    #     )
    #     ele_signup_home_click.click()
    #     signup.SignupPage.fill_signup_details(appium_driver)
    #     signin.SigninPage.test_enter_signin_info(appium_driver)
    #
    # def test_signin_with_pass(self,appium_driver):
    #     ele_login_with_pass_click = WebDriverWait(appium_driver, 20).until(
    #         EC.element_to_be_clickable(
    #             (AppiumBy.XPATH, '//android.widget.TextView[@text="Login with Password"]'
    #     ))
    #     )
    #     ele_login_with_pass_click.click()
    #     signin.SigninPage.test_sign_with_password(appium_driver)
    #
    #
    # def test_already_account (self,appium_driver):
    #     ele_signup_home_click = WebDriverWait(appium_driver, 20).until(
    #         EC.element_to_be_clickable(
    #             (AppiumBy.XPATH, '//android.widget.TextView[@text="Sign up"]'
    #              ))
    #     )
    #     ele_signup_home_click.click()
    #     ele_login_button = WebDriverWait(appium_driver, 20).until(
    #         EC.element_to_be_clickable(
    #             (AppiumBy.XPATH, '//android.widget.TextView[@text=" Login"]'
    #              ))
    #     )
    #     ele_login_button.click()
    #     ele_login_with_pass_click = WebDriverWait(appium_driver, 20).until(
    #         EC.element_to_be_clickable(
    #             (AppiumBy.XPATH, '//android.widget.TextView[@text="Login with Password"]'
    #              ))
    #     )
    #     ele_login_with_pass_click.click()
    #     signin.SigninPage.test_sign_with_password(appium_driver)
    #
    # def test_searchbox_products(self, appium_driver):
    #     ele_press_search = WebDriverWait(appium_driver, 20).until(
    #         EC.presence_of_element_located(
    #             (AppiumBy.XPATH, '//android.widget.EditText[@text="Search for Over 5000 Product"]')
    #         )
    #     )
    #     ele_press_search.click()
    #     ele_search_prod = WebDriverWait(appium_driver, 20).until(
    #         EC.presence_of_element_located(
    #             (AppiumBy.XPATH, '//android.widget.EditText[@text="Search"]')
    #         )
    #     )
    #     ele_search_prod.send_keys('Biscuits')
    #     # ele_search_prod.send_keys(Keys.ENTER)
    #
    # def test_favourite_item (self,appium_driver):
    #     ele_add_favourite_item =  WebDriverWait(appium_driver, 20).until(
    #         EC.presence_of_element_located(
    #             (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="addCartFav205"]/android.widget.ImageView')
    #         )
    #     )
    #     ele_add_favourite_item.click()
    #     ele_added_item_successfully = WebDriverWait(appium_driver, 20).until(
    #         EC.presence_of_element_located(
    #             (AppiumBy.XPATH, '//android.widget.TextView[@text="OK"]')
    #         )
    #     )
    #     ele_added_item_successfully.click()
    #     ele_select_add_cart = WebDriverWait(appium_driver, 20).until(
    #         EC.presence_of_element_located(
    #             (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup[6]')
    #         )
    #     )
    #     ele_select_add_cart.click()
    #     ele_continue_for_order_place = WebDriverWait(appium_driver, 20).until(
    #         EC.presence_of_element_located(
    #             (AppiumBy.XPATH, '//android.widget.TextView[@text="CONTINUE"]')
    #         )
    #     )
    #     ele_continue_for_order_place.click()
    #     print("Test for favourite item adding to cart passed")
    #
    # def test_account_signout_button(self, appium_driver):
    #     ele_account_click = WebDriverWait(appium_driver, 20).until(
    #             EC.element_to_be_clickable(
    #                 (AppiumBy.XPATH,
    #                  '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.ImageView')
    #             )
    #         )
    #     ele_account_click.click()
    #     print("Clicked on account signout button successfully")
    #     ele_click_signout = WebDriverWait(appium_driver, 20).until(
    #             EC.element_to_be_clickable(
    #                 (AppiumBy.XPATH,
    #                  '//android.widget.TextView[@text="Signout"]')
    #             )
    #     )
    #     ele_click_signout.click()
    #
    # def test_cart_browser(self, appium_driver):
    #     ele_click_cart_image = WebDriverWait(appium_driver, 20).until(
    #             EC.element_to_be_clickable(
    #                 (AppiumBy.XPATH,
    #                  '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ImageView')
    #             )
    #         )
    #     ele_click_cart_image.click()
    #
    #
    #
