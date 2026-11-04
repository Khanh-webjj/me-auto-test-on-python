from core.driver.appium_driver import create_driver
from pages.onboarding_page.onboarding_page import OnboardingPage
from pages.home_page.home_page import HomePage
from core.util.config import Config

def test_complete_onboarding_flow():
    driver = None

    try: 
        driver = create_driver()

        driver.activate_app(Config().app_package)

        onboarding = OnboardingPage(driver)

        assert onboarding.is_displayed(), (
            "App didnt display onboarding screen 1st"
        )

        for current_page in range(1,4):
            onboarding.tap_continue_button()

            if current_page < 4:
                next_page = current_page + 1

                assert onboarding.is_onboarding_page_displayed(next_page), (
                    f"App didnt display onboarding screen {next_page} after tapping continue button on screen {current_page}"
                )

        home_page = HomePage(driver)
        assert home_page.is_displayed(), (
            "App didnt display home screen after tapping continue button on screen 4"
        )

        print("Onboarding flow test passed successfully.")

    finally:
        if driver is not None:
            driver.quit()
        