import pytest
from core.driver.appium_driver import create_driver

@pytest.fixture
def driver():
    driver = create_driver()

    yield driver
    
    driver.quit()