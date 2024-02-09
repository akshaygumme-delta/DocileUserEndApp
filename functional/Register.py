from Driver.appiumandroid import AppiumDriverManager
from Pages.elementsaccess import AppiumElementFinder
import logging
import openpyxl
from openpyxl.styles import Font

logging.basicConfig(filename='test_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = 'Test Results'

headers = ['Issue ID', 'Issue Description', 'Test Result', 'Screenshot', 'Severity Level',
           'Steps to Reproduce', 'Expected Behavior', 'Actual Behavior', 'Device/Platform',
           'Additional Notes/Comments']
sheet.append(headers)

for col in range(1, len(headers) + 1):
    sheet.cell(row=1, column=col).font = Font(bold=True)


def write_test_result(issue_id, issue_description, test_result, screenshot, severity_level,
                      steps_to_reproduce, expected_behavior, actual_behavior, device_platform,
                      additional_notes_comments):
    sheet.append([issue_id, issue_description, test_result, screenshot, severity_level,
                  steps_to_reproduce, expected_behavior, actual_behavior, device_platform,
                  additional_notes_comments])
    workbook.save('testcase_results.xlsx')


def test_successful_login():
    try:
        driver_manager = AppiumDriverManager()
        driver = driver_manager.appium_driver()
        element_finder = AppiumElementFinder(driver)

        login_xpaths = ['//android.widget.TextView[@text="Docile"]', '//android.widget.TextView[@text="Get Started"]',
                        '//android.widget.TextView[@text="Sign in"]']
        for xpath in login_xpaths:
            element_finder.find_clickable_element_by_xpath(xpath).click()

        element_finder.find_send_data_by_xpath('//android.widget.EditText[@text="Phone Number"]').send_keys(
            "7972951602")

        element_finder.find_clickable_element_by_xpath('//android.widget.Button[@text="Continue"]').click()
        element_finder.find_clickable_element_by_xpath('//android.widget.Button[@text="Next"]').click()

        welcome_message = element_finder.find_visible_element_by_xpath(
            '//android.widget.TextView[contains(@text, "Sit Tight! We\'re Coming Soon ")]').text
        assert "Welcome" in welcome_message, "Login was not successful"
        logging.info("Successful login test passed")

        # Write test result to Excel
        write_test_result(issue_id='1', issue_description='Login with valid credentials',
                          test_result='Passed', screenshot='screenshot1.png',
                          severity_level='Low', steps_to_reproduce='1. Open app\n2. Enter valid credentials',
                          expected_behavior='User should be logged in successfully',
                          actual_behavior='User logged in successfully',
                          device_platform='Android', additional_notes_comments='No issues')

    except Exception as e:
        logging.error(f"Failed to execute successful login test: {e}")

        # Write test result to Excel
        write_test_result(issue_id='1', issue_description='Login with valid credentials',
                          test_result='Failed', screenshot='screenshot1.png',
                          severity_level='High', steps_to_reproduce='1. Open app\n2. Enter valid credentials',
                          expected_behavior='User should be logged in successfully',
                          actual_behavior='Login failed',
                          device_platform='Android', additional_notes_comments='Error encountered')


def test_invalid_login():
    try:
        driver_manager = AppiumDriverManager()
        driver = driver_manager.appium_driver()
        element_finder = AppiumElementFinder(driver)

        login_xpaths = ['//android.widget.TextView[@text="Docile"]', '//android.widget.TextView[@text="Get Started"]',
                        '//android.widget.TextView[@text="Sign in"]']
        for xpath in login_xpaths:
            element_finder.find_clickable_element_by_xpath(xpath).click()

        element_finder.find_send_data_by_xpath('//android.widget.EditText[@text="Phone Number"]').send_keys("87878778**")

        error_message = element_finder.find_visible_element_by_xpath(
            '//android.widget.TextView[contains(@text, "Sit Tight! We\'re Coming soon")]').text
        assert "Invalid" in error_message, "Login was expected to fail with invalid credentials"
        logging.info("Invalid login test passed")

        # Write test result to Excel
        write_test_result(issue_id='2', issue_description='Login with invalid credentials',
                          test_result='Passed', screenshot='screenshot2.png',
                          severity_level='Medium', steps_to_reproduce='1. Open app\n2. Enter invalid credentials',
                          expected_behavior='Login should fail',
                          actual_behavior='Login failed as expected',
                          device_platform='Android', additional_notes_comments='No issues')

    except Exception as e:
        # Log test failure
        logging.error(f"Failed to execute invalid login test: {e}")

        # Write test result to Excel
        write_test_result(issue_id='2', issue_description='Login with invalid credentials',
                          test_result='Failed', screenshot='screenshot2.png',
                          severity_level='High', steps_to_reproduce='1. Open app\n2. Enter invalid credentials',
                          expected_behavior='Login should fail',
                          actual_behavior='Login did not fail as expected',
                          device_platform='Android', additional_notes_comments='Error encountered')

