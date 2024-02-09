# # import pytest
# # from appium import webdriver
# # from appium.options.common.base import AppiumOptions
# # from appium.webdriver.common.appiumby import AppiumBy
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from appium.webdriver.common.touch_action import TouchAction
# # from Pages import getstarted,signup,signin,forgotpassword,browserproducts,addtocart,enteraddress
# # from selenium.webdriver.common.keys import Keys
# # import main
# # @pytest.fixture(scope="module")
# # def appium_driver():
# #     options = AppiumOptions()
# #     options.load_capabilities({
# #             "platformName": "Android",
# #             "deviceName": "adb-10BD9D2K350007X-mczaYj._adb-tls-connect._tcp",
# #
# #         })
# #     # Add other desired capabilities as needed
# #
# #     driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
# #     yield driver
# #     # driver.quit()
# #
# #
# # @pytest.mark.usefixtures("appium_driver")
# # class Testunittestcases:
# #     @staticmethod
# #     def test_register_user_tc001(appium_driver):
# #         main.TestAppiumAutomation.test_click_docile_element(appium_driver)
# #         getstarted.start.test_click_get_started_element(appium_driver)
# #         ele_signup_home_click = WebDriverWait(appium_driver, 20).until(
# #                 EC.element_to_be_clickable(
# #                     (AppiumBy.XPATH, '//android.widget.TextView[@text="Sign up"]'
# #                      ))
# #             )
# #         ele_signup_home_click.click()
# #         signup.SignupPage.fill_signup_details(appium_driver)
# #         signin.SigninPage.test_enter_signin_info(appium_driver)
# #         main.TestAppiumAutomation.test_close_app(appium_driver)
# import pytest
# import inspect
# from appium import webdriver
# from appium.options.common.base import AppiumOptions
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from openpyxl import Workbook, load_workbook
# from Pages import get
# # Load the existing Excel workbook
# wb = load_workbook("automation_test_report_ss.xlsx")
# ws = wb.active
#
# def execute_test_case(test_function, test_id):
#     try:
#         test_function()
#         print('Test case executed successfully')
#         result = "Pass"
#     except TimeoutException:
#         print("TimeoutException: Element not found within the specified timeout")
#         result = "Fail"
#
#     screenshot_name = f"test_click_docile_element_tc_{test_id}.png"
#     appium_driver.save_screenshot(screenshot_name)
#
#     function_name = test_function.__name__
#     screenshot_hyperlink = f'=HYPERLINK("{screenshot_name}", "Screenshot_tc{test_id}.png")'
#     ws.append([f"TC-{test_id}", function_name, result, screenshot_hyperlink])
#     wb.save("automation_test_report_ss.xlsx")
#
# # Define a fixture to save the workbook after the tests have run
# @pytest.fixture(scope="session")
# def excel_results(request):
#     def fin():
#         wb.save("automation_test_report_ss.xlsx")
#         wb.close()
#     request.addfinalizer(fin)
#
# # Define a fixture to open the appium driver
# @pytest.fixture(scope="module")
# def appium_driver():
#     options = AppiumOptions()
#     options.load_capabilities({
#         "platformName": "Android",
#         "deviceName": "RZ8R21SMYNN",
#     })
#
#     driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
#     yield driver
#     driver.quit()
#
# @pytest.mark.usefixtures("appium_driver", "excel_results")
# class TestAppiumAutomation:
#     @staticmethod
#     def test_click_docile_element_tc_01(appium_driver):
#         def actual_test_function():
#             el = WebDriverWait(appium_driver, 20).until(
#                 EC.element_to_be_clickable((
#                     AppiumBy.XPATH, '(//android.widget.TextView[@content-desc="Docile"])'
#                 ))
#             )
#             el.click()
#             WebDriverWait(appium_driver, 20).until(
#                 EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Get Started"]'))
#             )
#             print("App started Successfully")
#             assert True  # Example assertion
#
#         execute_test_case(actual_test_function, "01")
#
#     def test_getting_start_element_tc_02(self, appium_driver):
#         def actual_test_function():
#             getstarted.start.test_click_get_started_element(appium_driver)
#             print('Getting Started button successfully clicked')
#             assert True  # Example assertion
#
#         execute_test_case(actual_test_function, "02")
