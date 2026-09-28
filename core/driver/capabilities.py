from appium.options.android import UiAutomator2Options

from core.util.config import Config

def get_android_options():
    config = Config()

    options = UiAutomator2Options()

    options.platform_name = config.platform_name
    options.automation_name = config.automation_name
    options.device_name = config.device_name
    options.app_package = config.app_package
    
    options.no_reset = config.no_reset
    options.auto_grant_permissions = config.auto_grant_permissions

    return options