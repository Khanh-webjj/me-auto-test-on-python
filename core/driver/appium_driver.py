from appium import webdriver
from appium.options.android import UiAutomator2Options

APPIUM_SERVER_URL = "http://127.0.0.1:4723"

def create_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.duygiangdg.magiceraser"

    driver = webdriver.Remote(
        command_executor=APPIUM_SERVER_URL, 
        options=options)
    return driver