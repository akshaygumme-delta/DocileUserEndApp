from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignupPage:
    @staticmethod
    def fill_signup_details(appium_driver):
        ele_select_individual = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="TestIndividual"]'))
        )
        ele_select_individual.click()

        ele_full_name = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@text="Enter your full name"]'))
        )

        # Clear any existing text in the input field (optional)
        ele_full_name.clear()

        # Enter the full name into the input field
        ele_full_name.send_keys('Akshay Gumme')

        # Call the enter_mobile_no method from the TestAppiumAutomation class
        ele_mobile_no = WebDriverWait(appium_driver, 20).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Phone Number"]'))
        )

        # Clear any existing text in the input field (optional)
        ele_mobile_no.clear()

        # Enter the mobile number into the input field
        ele_mobile_no.send_keys('7972951602')

        ele_select_next_button = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Next"]'))
        )
        ele_select_next_button.click()

        ele_continue_with_mobile_no = WebDriverWait(appium_driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="CONTINUE WITH +917972951602"]'))
        )

        ele_continue_with_mobile_no.click()
