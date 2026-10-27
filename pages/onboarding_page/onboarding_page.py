from pages.base_page import BasePage
from pages.onboarding_page.onboarding_page_locators import OnboardingPageLocators


class OnboardingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_displayed(self):
        return super().is_displayed(OnboardingPageLocators.root())

    def tap_continue_button(self):
        super().click(OnboardingPageLocators.continue_button())

    def get_text_of_feature_title(self):
        return super().get_attribute(OnboardingPageLocators.feature_title, 'text')


    def get_text_of_feature_description(self):
        return super().get_attribute(OnboardingPageLocators.feature_discribe, 'text')