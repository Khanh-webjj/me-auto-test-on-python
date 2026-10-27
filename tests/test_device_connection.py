import pytest
from core.driver.appium_driver import create_driver


def test_device_connection(): 
    driver = None

    try: 
        driver = create_driver()

        # check Appium session
        assert (driver.session_id is not None, 
            "Appium session has not created yet")

        # check device
        capabilities = driver.capabilities
        print(f"Session ID: {driver.session_id}")
        print(f"Platform: {capabilities.get('platformName')}")
        print(f"Device: {capabilities.get('deviceName')}")
        print(f"Automation: {capabilities.get('appium:automationName')}")

        # send command to device to confirm connection
        current_package = driver.current_package

        assert (current_package is not None, 
            "Coudnt get current package")

        print(f"Current package: {current_package}")
        print(f"Appium connect to device success!")

    finally:
        if driver is not None:
            driver.quit()