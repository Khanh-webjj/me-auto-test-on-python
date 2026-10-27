from core.driver.appium_driver import create_driver
from pages.onboarding_page.onboarding_page import OnboardingPage
from core.util.config import Config

def test_complete_onboarding_flow():
    driver = None

    try: 
        driver = create_driver()

        driver.activate_app(Config.app_package)

        onboarding = OnboardingPage(driver)

        assert onboarding.is_displayed(), (
            "App didnt display onboarding screen 1st"
        )

        for current_page in range(1,5):
            onboarding.tap_continue_button()

            if current_page < 4:
                next_page = current_page + 1