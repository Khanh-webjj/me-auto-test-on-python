from appium.webdriver.common.appiumby import AppiumBy
from pygments.token import String
from pytest import Config


class HomePageLocators:
    app_package = Config.app_package()

    __ROOT_ID = f"{app_package}:id/sv_fragment"
    __MENU_BUTTON_ID = f"{app_package}:id/iv_menu"
    __PRO_BUTTON_ID = f"{app_package}:id/iv_pro"

    __COVER_ID = f"{app_package}:id/iv_image_before"
    __COVER_TITLE_ID = f"{app_package}:id/tv_top_title"
    __TRY_NOW_BUTTON_ID = f"{app_package}:id/tv_try_now"

    __REMOVE_OBJECTS_BUTTON_ID = f"{app_package}:id/btn_primary_remove"
    __REMOVE_BACKGROUND_BUTTON_ID = f"{app_package}:id/btn_primary_background"
    __START_EDITING_BUTTON_ID = f"{app_package}:id/btn_start_editing"

    __SECONDARY_ACTIONS_SCROLLVIEW_ID = f"{app_package}:id/rv_secondary_actions"
    __AI_ENHANCE_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"AI Enhance\"]"
    __AI_REPLACE_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"AI Replace\"]"
    __COLLAGE_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"Collage\"]"
    __DESIGN_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"Design\"]"
    __FILTER_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"Filter\"]"
    __BLUR_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"Blur\"]"
    __BRUSHES_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"Brushes\"]"
    __CROP_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"Crop\"]"
    __STICKER_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"Sticker\"]"
    __AI_FILTERS_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"AI Filters\"]"
    __AI_EXPAND_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"AI Expand\"]"
    __AI_GENERATE_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"AI Generate\"]"
    __FRAME_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"Frame\"]"
    __ADJUST_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"Adjust\"]"
    __TEXTURE_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"Texture\"]"
    __RESHAPE_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"Reshape\"]"
    __TEXT_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"Text\"]"
    __BASIC_EDIT_BUTTON_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_secondary_title\" and @text=\"Basic Edit\"]"

    __REMOVE_BACKGROUND_BANNER_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_basic_tools\" and @text=\"Remove Background\"]"
    __REMOVE_OBJECTS_BANNER_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_basic_tools\" and @text=\"Remove Objects\"]"
    __AI_ENHANCE_BANNER_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_basic_tools\" and @text=\"AI Enhance\"]"
    __AI_EXPAND_BANNER_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_basic_tools\" and @text=\"AI Expand\"]"
    __BASIC_EDIT_BANNER_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_basic_tools\" and @text=\"Basic Edit\"]"
    __AI_GENERATE_BANNER_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_basic_tools\" and @text=\"AI Generate\"]"
    __AI_FILTERS_BANNER_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_basic_tools\" and @text=\"AI Filters\"]"
    __AI_FILL_BANNER_XPATH = f"//android.widget.TextView[@resource-id=\"{app_package}:id/tv_basic_tools\" and @text=\"AI Fill\"]"

    __HOME_TAB_ID = f"{app_package}:id/ll_home";
    __TEMPLATE_TAB_ID = f"{app_package}:id/ll_template";
    __AI_FILTERS_TAB_ID = f"{app_package}:id/ll_ai_filter";
    __AI_GENERATE_TAB_ID = f"{app_package}:id/ll_ai_generate";

    @staticmethod
    def root():
        return AppiumBy.ID, HomePageLocators.__ROOT_ID

    @staticmethod
    def menu_button():
        return AppiumBy.ID, HomePageLocators.__MENU_BUTTON_ID    

    @staticmethod
    def pro_button():
        return AppiumBy.ID, HomePageLocators.__PRO_BUTTON_ID

    @staticmethod
    def cover():
        return AppiumBy.ID, HomePageLocators.__COVER_ID

    @staticmethod
    def cover_title():
        return AppiumBy.ID, HomePageLocators.__COVER_TITLE_ID

    @staticmethod
    def try_now_button():
        return AppiumBy.ID, HomePageLocators.__TRY_NOW_BUTTON_ID

    @staticmethod
    def remove_objects_button():
        return AppiumBy.ID, HomePageLocators.__REMOVE_OBJECTS_BUTTON_ID

    @staticmethod
    def remove_background_button():
        return AppiumBy.ID, HomePageLocators.__REMOVE_BACKGROUND_BUTTON_ID

    @staticmethod
    def start_editing_button():
        return AppiumBy.ID, HomePageLocators.__START_EDITING_BUTTON_ID

    @staticmethod
    def secondary_actions_scrollview():
        return AppiumBy.ID, HomePageLocators.__SECONDARY_ACTIONS_SCROLLVIEW_ID

    @staticmethod
    def ai_enhance_button():
        return AppiumBy.XPATH, HomePageLocators.__AI_ENHANCE_BUTTON_XPATH

    @staticmethod
    def ai_replace_button():
        return AppiumBy.XPATH, HomePageLocators.__AI_REPLACE_BUTTON_XPATH

    @staticmethod
    def collage_button():
        return AppiumBy.XPATH, HomePageLocators.__COLLAGE_BUTTON_XPATH

    @staticmethod
    def design_button():
        return AppiumBy.XPATH, HomePageLocators.__DESIGN_BUTTON_XPATH

    @staticmethod
    def filter_button():
        return AppiumBy.XPATH, HomePageLocators.__FILTER_BUTTON_XPATH

    @staticmethod
    def blur_button():
        return AppiumBy.XPATH, HomePageLocators.__BLUR_BUTTON_XPATH

    @staticmethod
    def brushes_button():
        return AppiumBy.XPATH, HomePageLocators.__BRUSHES_BUTTON_XPATH

    @staticmethod
    def crop_button():
        return AppiumBy.XPATH, HomePageLocators.__CROP_BUTTON_XPATH

    @staticmethod
    def sticker_button():
        return AppiumBy.XPATH, HomePageLocators.__STICKER_BUTTON_XPATH

    @staticmethod
    def ai_filters_button():
        return AppiumBy.XPATH, HomePageLocators.__AI_FILTERS_BUTTON_XPATH

    @staticmethod
    def ai_expand_button():
        return AppiumBy.XPATH, HomePageLocators.__AI_EXPAND_BUTTON_XPATH

    @staticmethod
    def ai_generate_button():
        return AppiumBy.XPATH, HomePageLocators.__AI_GENERATE_BUTTON_XPATH

    @staticmethod
    def frame_button():
        return AppiumBy.XPATH, HomePageLocators.__FRAME_BUTTON_XPATH

    @staticmethod
    def adjust_button():
        return AppiumBy.XPATH, HomePageLocators.__ADJUST_BUTTON_XPATH

    @staticmethod
    def texture_button():
        return AppiumBy.XPATH, HomePageLocators.__TEXTURE_BUTTON_XPATH

    @staticmethod
    def reshape_button():
        return AppiumBy.XPATH, HomePageLocators.__RESHAPE_BUTTON_XPATH

    @staticmethod
    def text_button():
        return AppiumBy.XPATH, HomePageLocators.__TEXT_BUTTON_XPATH

    @staticmethod
    def basic_edit_button():
        return AppiumBy.XPATH, HomePageLocators.__BASIC_EDIT_BUTTON_XPATH

    @staticmethod
    def remove_background_banner():
        return AppiumBy.XPATH, HomePageLocators.__REMOVE_BACKGROUND_BANNER_XPATH

    @staticmethod
    def remove_objects_banner():
        return AppiumBy.XPATH, HomePageLocators.__REMOVE_OBJECTS_BANNER_XPATH

    @staticmethod
    def ai_enhance_banner():
        return AppiumBy.XPATH, HomePageLocators.__AI_ENHANCE_BANNER_XPATH

    @staticmethod
    def ai_expand_banner():
        return AppiumBy.XPATH, HomePageLocators.__AI_EXPAND_BANNER_XPATH

    @staticmethod
    def basic_edit_banner():
        return AppiumBy.XPATH, HomePageLocators.__BASIC_EDIT_BANNER_XPATH

    @staticmethod
    def ai_generate_banner():
        return AppiumBy.XPATH, HomePageLocators.__AI_GENERATE_BANNER_XPATH

    @staticmethod
    def ai_filters_banner():
        return AppiumBy.XPATH, HomePageLocators.__AI_FILTERS_BANNER_XPATH

    @staticmethod
    def ai_fill_banner():
        return AppiumBy.XPATH, HomePageLocators.__AI_FILL_BANNER_XPATH

    @staticmethod
    def home_tab():
        return AppiumBy.ID, HomePageLocators.__HOME_TAB_ID    

    @staticmethod
    def template_tab():
        return AppiumBy.ID, HomePageLocators.__TEMPLATE_TAB_ID

    @staticmethod
    def ai_filters_tab():
        return AppiumBy.ID, HomePageLocators.__AI_FILTERS_TAB_ID

    @staticmethod
    def ai_generate_tab():
        return AppiumBy.ID, HomePageLocators.__AI_GENERATE_TAB_ID