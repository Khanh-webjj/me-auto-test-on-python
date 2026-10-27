from appium.webdriver.common.appiumby import AppiumBy


class OnboardingPageLocators:
    app_package = "com.duygiangdg.magiceraser"

    __ROOT_ID__ = f"{app_package}:id/root"
    __CONTINUE_BUTTON_ID__ = f"{app_package}:id/tv_onboard_continue"
    __FEATURE_TITLE_ID__ = f"{app_package}:id/tv_feature_title"
    __FEATURE_DISCRIBE_ID__ = f"{app_package}:id/tv_feature_desc"
    __FEATURE_OPTIONS_XPATH__ = f"//androidx.recyclerview.widget.RecyclerView[@resource-id=\"{app_package}:id/rv_feature\"]//android.widget.FrameLayout"
    __HANDLE_SLIDER_ID__ = f"{app_package}:id/iv_hand_slider"

    @staticmethod
    def root():
        return AppiumBy.ID, OnboardingPageLocators.__ROOT_ID__

    @staticmethod
    def continue_button():
        return AppiumBy.ID, OnboardingPageLocators.__CONTINUE_BUTTON_ID__

    @staticmethod
    def feature_title():
        return AppiumBy.ID, OnboardingPageLocators.__FEATURE_TITLE_ID__

    @staticmethod
    def feature_discribe():
        return AppiumBy.ID, OnboardingPageLocators.__FEATURE_DISCRIBE_ID__