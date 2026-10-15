from appium.webdriver.common.appiumby import AppiumBy

from core.util.config import Config


class PhotoEditorPageLocators:
    app_package = Config.app_package()

    ROOT_ID = f"{app_package}:id/photo_editor_root"

    MAIN_PANEL_ID = f"{app_package}:id/cl_photo_editor_tools"
    MAIN_PANEL_HORIZONTAL_SCROLL_VIEW_XPATH = f"{app_package}:id/hsv_main_tools"
    LAYER_BUTTON_XPATH = f"//androidx.cardview.widget.CardView[@resource-id='{app_package}:id/btn_layer']/android.widget.ImageView"
    INSERT_BUTTON_XPATH = f"{app_package}:id/fl_tool_add"
    CROP_BUTTON_XPATH = f"//android.widget.LinearLayout[@resource-id='{app_package}:id/tab_crop']/android.widget.FrameLayout"
    CLEANUP_BUTTON_XPATH = f"//android.widget.LinearLayout[@resource-id='{app_package}:id/tab_cleanup']/android.view.ViewGroup"
    RESHAPE_BUTTON_XPATH = f"//android.widget.LinearLayout[@resource-id='{app_package}:id/tab_reshape']/android.view.ViewGroup"
    AI_ENHANCE_BUTTON_XPATH = f"//android.widget.LinearLayout[@resource-id='{app_package}:id/tab_enhance']/android.view.ViewGroup"
    AI_EXPAND_BUTTON_XPATH = f"//android.widget.LinearLayout[@resource-id='{app_package}:id/tab_expand']/android.view.ViewGroup"
    ADJUST_BUTTON_XPATH = f"//android.widget.LinearLayout[@resource-id='{app_package}:id/tab_adjust']/android.view.ViewGroup"
    PARTIAL_BUTTON_XPATH = f"//android.widget.LinearLayout[@resource-id='{app_package}:id/tab_partial']/android.view.ViewGroup"
    HSL_BUTTON_XPATH = f"//android.widget.LinearLayout[@resource-id='{app_package}:id/tab_hsl']/android.view.ViewGroup"
    WB_BUTTON_XPATH = f"//android.widget.LinearLayout[@resource-id='{app_package}:id/tab_white_balance']/android.view.ViewGroup"
    FILTER_BUTTON_XPATH = f"//android.widget.LinearLayout[@resource-id='{app_package}:id/tab_filter']/android.view.ViewGroup"
    BLUR_BUTTON_XPATH = f"//android.widget.LinearLayout[@resource-id='{app_package}:id/tab_blur']/android.view.ViewGroup"
    TEXTURE_BUTTON_XPATH = f"//android.widget.LinearLayout[@resource-id='{app_package}:id/tab_texture']/android.view.ViewGroup"
    FRAME_BUTTON_XPATH = f"//android.widget.LinearLayout[@resource-id='{app_package}:id/tab_frame']/android.widget.FrameLayout"
    BRUSHES_BUTTON_XPATH = f"//android.widget.LinearLayout[@resource-id='{app_package}:id/tab_brush']/android.widget.FrameLayout"

    CANVAS_ID = f"{app_package}:id/meCanvas"
    BACK_BUTTON_ID = f"{app_package}:id/btn_back"
    UNDO_BUTTON_ID = f"{app_package}:id/ib_undo"
    REDO_BUTTON_ID = f"{app_package}:id/ib_redo"
    COMPARE_BUTTON_ID = f"{app_package}:id/ib_compare"
    SAVE_BUTTON_ID = f"{app_package}:id/btn_save"

    @staticmethod
    def root():
        return AppiumBy.ID, PhotoEditorPageLocators.ROOT_ID

    @staticmethod
    def main_panel():
        return AppiumBy.ID, PhotoEditorPageLocators.MAIN_PANEL_ID

    @staticmethod  
    def main_panel_horizontal_scroll_view():
            return AppiumBy.ID, PhotoEditorPageLocators.MAIN_PANEL_HORIZONTAL_SCROLL_VIEW_XPATH

    @staticmethod
    def layer_button():
        return AppiumBy.XPATH, PhotoEditorPageLocators.LAYER_BUTTON_XPATH

    @staticmethod
    def insert_button():
        return AppiumBy.XPATH, PhotoEditorPageLocators.INSERT_BUTTON_XPATH

    @staticmethod
    def crop_button():
        return AppiumBy.XPATH, PhotoEditorPageLocators.CROP_BUTTON_XPATH

    @staticmethod
    def cleanup_button():
        return AppiumBy.XPATH, PhotoEditorPageLocators.CLEANUP_BUTTON_XPATH

    @staticmethod
    def reshape_button():
        return AppiumBy.XPATH, PhotoEditorPageLocators.RESHAPE_BUTTON_XPATH

    @staticmethod
    def ai_enhance_button():
        return AppiumBy.XPATH, PhotoEditorPageLocators.AI_ENHANCE_BUTTON_XPATH

    @staticmethod
    def ai_expand_button():
        return AppiumBy.XPATH, PhotoEditorPageLocators.AI_EXPAND_BUTTON_XPATH

    @staticmethod
    def adjust_button():
        return AppiumBy.XPATH, PhotoEditorPageLocators.ADJUST_BUTTON_XPATH

    @staticmethod
    def partial_button():
        return AppiumBy.XPATH, PhotoEditorPageLocators.PARTIAL_BUTTON_XPATH

    @staticmethod
    def hsl_button():
        return AppiumBy.XPATH, PhotoEditorPageLocators.HSL_BUTTON_XPATH

    @staticmethod
    def wb_button():
        return AppiumBy.XPATH, PhotoEditorPageLocators.WB_BUTTON_XPATH

    @staticmethod
    def filter_button():
        return AppiumBy.XPATH, PhotoEditorPageLocators.FILTER_BUTTON_XPATH

    @staticmethod
    def blur_button():
        return AppiumBy.XPATH, PhotoEditorPageLocators.BLUR_BUTTON_XPATH

    @staticmethod
    def texture_button():
        return AppiumBy.XPATH, PhotoEditorPageLocators.TEXTURE_BUTTON_XPATH

    @staticmethod
    def frame_button():
        return AppiumBy.XPATH, PhotoEditorPageLocators.FRAME_BUTTON_XPATH  

    @staticmethod
    def brushes_button():
        return AppiumBy.XPATH, PhotoEditorPageLocators.BRUSHES_BUTTON_XPATH    
