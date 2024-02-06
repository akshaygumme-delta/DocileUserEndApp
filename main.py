import time

import pytest
import inspect
import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook, load_workbook
from Pages import getstarted,cartpage,browserproducts,enteraddress,forgotpassword,signup,signin,addtocart
from selenium.common.exceptions import TimeoutException
# Load the existing Excel workbook
wb = load_workbook("automation_test_report_ss.xlsx")
ws = wb.active

# Define a fixture to save the workbook after the tests have run
@pytest.fixture(scope="session")
def excel_results(request):
    def fin():
        wb.save("automation_test_report_ss.xlsx")
        wb.close()


    request.addfinalizer(fin)

# Define a fixture to open the appium driver
@pytest.fixture(scope="module")
def appium_driver():
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "deviceName": "RZ8R21SMYNN",
    })

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    yield driver
    driver.quit()

@pytest.mark.usefixtures("appium_driver", "excel_results")
class TestAppiumAutomation:
    @staticmethod
    def test_click_docile_element_tc_01(appium_driver, excel_results):
        try:
            el = WebDriverWait(appium_driver, 20).until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH, '(//android.widget.TextView[@content-desc="Docile"])'
                ))
            )
            el.click()
            WebDriverWait(appium_driver, 20).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Get Started"]'))
            )
            screenshot_name = f"test_click_docile_element_tc_01.png"
            allure.attach(appium_driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            appium_driver.save_screenshot(screenshot_name)

            print("App started Successfully")
            assert True  # Example assertion
            result = "Pass"
            function_name = inspect.stack()[0][3]
            test_id = function_name.split("_")[-1]
            screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot")'
            ws.append([f"TC-{test_id}", function_name, result,screenshot_hyperlink])
            wb.save("automation_test_report_ss.xlsx")
        except TimeoutException:
            print("TimeoutException: Element not found within the specified timeout")
            result = "Fail"
        except AssertionError:
            print("AssertionError: Test assertion failed")
            result = "Fail"
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            result = "Fail"
        # finally:
        #     function_name = inspect.stack()[0][3]
        #     test_id = function_name.split("_")[-1]
        #     ws.append([f"TC-{test_id}", function_name, result,screenshot_name])
        #     wb.save("test_results.xlsx")


    def test_getting_start_element_tc_02(self, appium_driver):
        try:
            getstarted.start.test_click_get_started_element(appium_driver)
            allure.attach(appium_driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            print('Getting Started button successfully clicked')
            assert True  # Example assertion
            result = "Pass"


        except TimeoutException:
            print("TimeoutException: Element not found within the specified timeout")
            result = "Fail"
        function_name = inspect.stack()[0][3]

        test_id = function_name.split("_")[-1]

        ws.append([f"TC-{test_id}", function_name, result])

    def test_add_to_cart_tc_03(self, appium_driver):
        try:
            addtocart.Addtocart.test_add_product(appium_driver)
            allure.attach(appium_driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            print("item added to cart successfully")
            assert True  # Example assertion
            result = "Pass"

        except TimeoutException:
            print("TimeoutException: Element not found within the specified timeout")
            result = "Fail"

        function_name = inspect.stack()[0][3]

        test_id = function_name.split("_")[-1]

        ws.append([f"TC-{test_id}", function_name, result])

    def test_address_and_payment_successful_tc_04(self, appium_driver):
        try:
            enteraddress.Address.test_enter_address(appium_driver)
            print('order placed successfully')
            assert True  # Example assertion
            result = "Pass"

        except TimeoutException:
            print("TimeoutException: Element not found within the specified timeout")
            result = "Fail"
        function_name = inspect.stack()[0][3]

        test_id = function_name.split("_")[-1]

        ws.append([f"TC-{test_id}", function_name, result])


    def test_close_app_tc_05(self, appium_driver):
        try:
            appium_driver.press_keycode(3)
            appium_driver.quit()
            assert True  # Example assertion
            result = "Pass"

        except TimeoutException:
            print("TimeoutException: Element not found within the specified timeout")
            result = "Fail"
        function_name = inspect.stack()[0][3]

        test_id = function_name.split("_")[-1]

        ws.append([f"TC-{test_id}", function_name, result])
    def test_signin_details_tc_06(self,appium_driver):
        try:
            ele_sign_in_click = WebDriverWait(appium_driver, 20).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="Sign in"]'
            ))
            )
            ele_sign_in_click.click()
            signin.SigninPage.test_enter_signin_info(appium_driver)
            assert True  # Example assertion
            result = "Pass"
        except TimeoutException:
            print("TimeoutException: Element not found within the specified timeout")
            result = "Fail"
        function_name = inspect.stack()[0][3]

        test_id = function_name.split("_")[-1]

        ws.append([f"TC-{test_id}", function_name, result])
    def test_signin_with_password_tc_07 (self,appium_driver):
        try:
            ele_sign_in_click = WebDriverWait(appium_driver, 20).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="Sign in"]'
                     ))
            )
            ele_sign_in_click.click()
            ele_login_with_pass_click = WebDriverWait(appium_driver, 20).until(
                        EC.element_to_be_clickable(
                            (AppiumBy.XPATH, '//android.widget.TextView[@text="Login with Password"]'
                             ))
                    )
            ele_login_with_pass_click.click()
            signin.SigninPage.test_sign_with_password(appium_driver)
            assert True  # Example assertion
            result = "Pass"
        except TimeoutException:
            print("TimeoutException: Element not found within the specified timeout")
            result = "Fail"

        function_name = inspect.stack()[0][3]

        test_id = function_name.split("_")[-1]

        ws.append([f"TC-{test_id}", function_name, result])

    def test_forgot_password_tc_08 (self, appium_driver):
        ele_sign_in_click = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Sign in"]'
                 ))
        )
        ele_sign_in_click.click()
        ele_login_with_pass_click = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Login with Password"]'
                 ))
        )
        ele_login_with_pass_click.click()
        forgotpassword.Forgotpassword.test_forgot_password(appium_driver)
    def test_current_location_tc (self,appium_driver):
        ele_change_location = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Hyderabad"]'))
        )
        ele_change_location.click()
        ele_current_location = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text=" Current Location"]'))
        )
        ele_current_location.click()
        ele_conf_continue = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH,
                 '//android.widget.TextView[@text="Confirm & Continue"]')
            )
        )
        ele_conf_continue.click()
        WebDriverWait(appium_driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="NotificationTest"]'))
        )
        print("Location change passed")


    def test_sight_tight_and_logout_tc009 (self,appium_driver):
        el = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, '(//android.widget.TextView[@content-desc="Docile"])[2]'
            ))
        )
        el.click()
        ele_get_started = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Get Started"]'))
        )
        ele_get_started.click()
        WebDriverWait(appium_driver, 20).until(
            EC.visibility_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Sit Tight! We\'re Coming soon!"]'))
        )
        print("sit Tight, we're coming soon test passed")
    #
    #
    #
    #
    def test_dont_hv_account(self, appium_driver):
        ele_dont_acc_sign_up = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Don\'t have an account? Sign Up"]'
        ))
        )
        ele_dont_acc_sign_up.click()
        signup.SignupPage.fill_signup_details(appium_driver)

    def test_signup_homepage_click(self, appium_driver):
        try:
            ele_signup_home_click = WebDriverWait(appium_driver, 20).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="Sign up"]'
            ))
            )
            ele_signup_home_click.click()
            signup.SignupPage.fill_signup_details(appium_driver)
            signin.SigninPage.test_enter_signin_info(appium_driver)
            assert True  # Example assertion
            result = "Pass"

        except AssertionError:
            result = "Fail"

        function_name = inspect.stack()[0][3]

        line_number = inspect.getframeinfo(inspect.currentframe()).lineno

        ws.append([f"TC-{line_number}", function_name, result])

    def test_signin_with_pass(self,appium_driver):
        ele_login_with_pass_click = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Login with Password"]'
        ))
        )
        ele_login_with_pass_click.click()
        signin.SigninPage.test_sign_with_password(appium_driver)


    def test_already_account_tc007 (self,appium_driver):
        ele_signup_home_click = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Sign up"]'
                 ))
        )
        ele_signup_home_click.click()
        ele_login_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text=" Login"]'
                 ))
        )
        ele_login_button.click()
        ele_login_with_pass_click = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="Login with Password"]'
                 ))
        )
        ele_login_with_pass_click.click()
        signin.SigninPage.test_sign_with_password(appium_driver)
    #
    def test_searchbox_products_tc_11(self, appium_driver):
        ele_press_search = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@text="Search for Over 5000 Product"]')
            )
        )
        ele_press_search.click()
        ele_search_prod = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@text="Search"]')
            )
        )
        ele_search_prod.send_keys('Biscuits')
        time.sleep(7)
        allure.attach(appium_driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)




    def test_favourite_item (self,appium_driver):
        ele_add_favourite_item =  WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="addCartFav205"]/android.widget.ImageView')
            )
        )
        ele_add_favourite_item.click()
        ele_added_item_successfully = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="OK"]')
            )
        )
        ele_added_item_successfully.click()
        ele_select_add_cart = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup[6]')
            )
        )
        ele_select_add_cart.click()
        ele_continue_for_order_place = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="CONTINUE"]')
            )
        )
        ele_continue_for_order_place.click()
        print("Test for favourite item adding to cart passed")

    def test_account_signout_button(self, appium_driver):
        ele_account_click = WebDriverWait(appium_driver, 20).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH,
                     '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup[7]')
                )
            )
        ele_account_click.click()
        print("Clicked on account signout button successfully")
        ele_click_signout = WebDriverWait(appium_driver, 20).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH,
                     '//android.widget.TextView[@text="Signout"]')
                )
        )
        ele_click_signout.click()
        ele_signout_ok = WebDriverWait(appium_driver, 20).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH,
                     '//android.widget.Button[@resource-id="android:id/button2"]')
                )
        )
        ele_signout_ok.click()

    def test_cart_browser(self, appium_driver):
        ele_click_cart_image = WebDriverWait(appium_driver, 20).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH,
                     '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ImageView')
                )
            )
        ele_click_cart_image.click()

    def test_expolre_categories(self,appium_driver):
        ele_click_category = WebDriverWait(appium_driver, 20).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH,
                     '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.ImageView')
                )
            )
        ele_click_category.click()
        ele_sub_category = WebDriverWait(appium_driver, 20).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH,'//android.view.ViewGroup[@resource-id="catogery1"]'))
        )
        ele_sub_category.click()
        ele_prod_click = WebDriverWait(appium_driver, 20).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH,'//android.widget.TextView[@text="Fresh Vegetables"]'))
        )
        ele_prod_click.click()
        WebDriverWait(appium_driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.ScrollView[@resource-id="sub_categories_list"]/android.view.ViewGroup/android.view.ViewGroup[1]'))
        )
        print("Explore Category test is passed")


