from appium import webdriver

from core.driver.capabilities import get_android_options
from core.util.config import Config

def create_driver():
    config = Config()
    options = get_android_options()

    return webdriver.Remote(
        command_executor=config.appium_server_url, 
        options=options    
    )

