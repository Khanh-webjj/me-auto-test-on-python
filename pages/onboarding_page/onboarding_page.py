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

    def is_onboarding_page_displayed(self, num_fear):
        if num_fear > 4 or num_fear < 1:
            return False

        if num_fear == 1:
            return (self.get_text_of_feature_title() == "Easy Remove Object" 
                and self.get_text_of_feature_description == "Select unwanted objects and remove objects")

        elif(num_fear == 2):
            return (self.get_text_of_feature_title() == "Enhance Quality" 
                and self.get_text_of_feature_description == "Elevate your images instantly—clarity and vibrance at your fingertips!")

        elif(num_fear == 3):
            return (self.get_text_of_feature_title() == "Remove Background" 
                and self.get_text_of_feature_description == "Instantly clean up your pictures! Tap 'Remove Background' to make your photos stand out.")

        elif(num_fear == 4):
            return (self.get_text_of_feature_title() == "AI Filter" 
                and self.get_text_of_feature_description == "Transform your images into various styles like anime, comic book, and more.")
        