from appium.options.android import UiAutomator2Options

def get_android_options():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.duygiangdg.magiceraser"
    
    return options