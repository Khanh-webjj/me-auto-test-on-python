from appium.webdriver.common.appiumby import AppiumBy

from core.util.config import Config


class BrushPanelLocators:
    app_package = Config.app_package()

    ROOT_ID = f"{app_package}:id/panel_brush"
    DONE_BUTTON_ID = f"{app_package}:id/tv_panel_done"
    SLIDER_XPATH = f"//android.widget.LinearLayout[./android.widget.TextView[@resource-id='{app_package}:id/tv_brush_size_label']]/android.widget.LinearLayout"
    BRUSH_MODE_BUTTON_ID = f"{app_package}:id/cv_brush_pen"
    ERASER_MODE_BUTTON_ID = f"{app_package}:id/cv_brush_eraser"
    COLOR_OPTION_LIST_XPATH = f"//androidx.recyclerview.widget.RecyclerView[@resource-id='{app_package}:id/rv_colors']/android.view.ViewGroup"
    BRUSH_STYLE_OPTION_LIST_XPATH = f"//androidx.recyclerview.widget.RecyclerView[@resource-id='{app_package}:id/rv_brush_list']/android.view.ViewGroup"
    COLOR_HORIZONTAL_VIEW_ID = f"{app_package}:id/rv_colors"
    BRUSH_HORIZONTAL_VIEW_ID = f"{app_package}:id/rv_brush_list"

    @staticmethod
    def root():
        return AppiumBy.ID, BrushPanelLocators.ROOT_ID

    @staticmethod
    def done_button():
        return AppiumBy.ID, BrushPanelLocators.DONE_BUTTON_ID

    @staticmethod
    def slider():
        return AppiumBy.XPATH, BrushPanelLocators.SLIDER_XPATH

    @staticmethod
    def brush_mode_button():
        return AppiumBy.ID, BrushPanelLocators.BRUSH_MODE_BUTTON_ID

    @staticmethod
    def eraser_mode_button():   
        return AppiumBy.ID, BrushPanelLocators.ERASER_MODE_BUTTON_ID

    @staticmethod
    def color_option_list():
        return AppiumBy.XPATH, BrushPanelLocators.COLOR_OPTION_LIST_XPATH

    @staticmethod
    def brush_style_option_list():          
        return AppiumBy.XPATH, BrushPanelLocators.BRUSH_STYLE_OPTION_LIST_XPATH

    @staticmethod
    def color_horizontal_view():
        return AppiumBy.ID, BrushPanelLocators.COLOR_HORIZONTAL_VIEW_ID

    @staticmethod
    def brush_horizontal_view():
        return AppiumBy.ID, BrushPanelLocators.BRUSH_HORIZONTAL_VIEW_ID

    