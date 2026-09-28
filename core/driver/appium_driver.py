from appium import webdriver
from core.driver.capabilities import get_android_options

APPIUM_SERVER_URL = "http://127.0.0.1:4723"

def create_driver():
    options = get_android_options()

    return webdriver.Remote(
        command_executor=APPIUM_SERVER_URL, 
        options=options)

