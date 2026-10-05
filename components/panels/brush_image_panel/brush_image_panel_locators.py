from appium.webdriver.common.appiumby import AppiumBy
from core.util.config import Config


class BrushPanelLocators:
    app_package = Config.app_package()

    ROOT_XPATH = f"//android.view.ViewGroup[@resource-id='{app_package}:id/view_image_panel' and .//android.widget.TextView[@text='Brush']]"
    DONE_BUTTON_XPATH = f"{ROOT_XPATH}//android.widget.Button[@resource-id='{app_package}:id/btn_done']"
    DUPLICATE_BUTTON_ID = f"{app_package}:id/fl_btn_duplicate"
    DELETE_BUTTON_ID = f"{app_package}:id/fl_btn_edit_layer_delete"
    LAYER_UP_BUTTON_ID = f"{app_package}:id/fl_layer_up"
    LAYER_DOWN_BUTTON_ID = f"{app_package}:id/fl_layer_down"
    LAYER_TOP_BUTTON_ID = f"{app_package}:id/fl_layer_top"
    LAYER_BOTTOM_BUTTON_ID = f"{app_package}:id/fl_layer_bottom"
    FLIP_VERTICAL_BUTTON_ID = f"{app_package}:id/fl_flip_vertical"
    FLIP_HORIZONTAL_BUTTON_ID = f"{app_package}:id/fl_flip_horizontal"

    EDIT_BUTTON_ID = f"{app_package}:id/fl_image_replace"
    OPACITY_BUTTON_ID = f"{app_package}:id/fl_image_opacity"
    ADJUST_BUTTON_ID = f"{app_package}:id/fl_image_adjust"
    OUTLINE_BUTTON_ID = f"{app_package}:id/fl_image_outline"
    SHADOW_BUTTON_ID = f"{app_package}:id/fl_image_shadow"
    REFLECTION_BUTTON_ID = f"{app_package}:id/fl_image_reflection"

    @staticmethod
    def root():
        return AppiumBy.XPATH, BrushPanelLocators.ROOT_XPATH

    @staticmethod
    def done_button():
        return AppiumBy.XPATH, BrushPanelLocators.DONE_BUTTON_XPATH

    @staticmethod
    def duplicate_button():
        return AppiumBy.ID, BrushPanelLocators.DUPLICATE_BUTTON_ID

    @staticmethod
    def delete_button():
        return AppiumBy.ID, BrushPanelLocators.DELETE_BUTTON_ID

    @staticmethod
    def layer_up_button():
        return AppiumBy.ID, BrushPanelLocators.LAYER_UP_BUTTON_ID

    @staticmethod
    def layer_down_button():
        return AppiumBy.ID, BrushPanelLocators.LAYER_DOWN_BUTTON_ID

    @staticmethod
    def layer_top_button():
        return AppiumBy.ID, BrushPanelLocators.LAYER_TOP_BUTTON_ID

    @staticmethod
    def layer_bottom_button():
        return AppiumBy.ID, BrushPanelLocators.LAYER_BOTTOM_BUTTON_ID

    @staticmethod
    def flip_vertical_button():
        return AppiumBy.ID, BrushPanelLocators.FLIP_VERTICAL_BUTTON_ID

    @staticmethod
    def flip_horizontal_button():
        return AppiumBy.ID, BrushPanelLocators.FLIP_HORIZONTAL_BUTTON_ID

    @staticmethod
    def edit_button():
        return AppiumBy.ID, BrushPanelLocators.EDIT_BUTTON_ID

    @staticmethod
    def opacity_button():
        return AppiumBy.ID, BrushPanelLocators.OPACITY_BUTTON_ID

    @staticmethod
    def adjust_button():
        return AppiumBy.ID, BrushPanelLocators.AJUST_BUTTON_ID

    @staticmethod
    def outline_button():
        return AppiumBy.ID, BrushPanelLocators.OUTLINE_BUTTON_ID

    @staticmethod
    def shadow_button():
        return AppiumBy.ID, BrushPanelLocators.SHADOW_BUTTON_ID

    @staticmethod
    def reflection_button():
        return AppiumBy.ID, BrushPanelLocators.REFLECTION_BUTTON_ID