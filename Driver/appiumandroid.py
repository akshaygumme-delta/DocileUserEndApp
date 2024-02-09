from appium import webdriver
from appium.options.common.base import AppiumOptions


class AppiumDriverManager:
    def appium_driver(self):
        options = AppiumOptions()
        options.load_capabilities({
            "platformName": "Android",
            "deviceName": "RZ8R21SMYNN",
        })

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
        return driver
