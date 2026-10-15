from pages.base_page import BasePage
from pages.home_page.home_page_locators import HomePageLocators
from core.util.gesture import Gesture

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_displayed(self):
        return super().is_displayed(HomePageLocators.root())

    #header
    def tap_menu_button(self):
        super().click(HomePageLocators.menu_button())

    def tap_pro_button(self):
        super().click(HomePageLocators.pro_button())

    def tap_cover(self):
        super().click(HomePageLocators.cover())

    def get_text_from_cover(self):
        return super().get_text(HomePageLocators.cover_title())

    def tap_try_now_button(self):
        super().click(HomePageLocators.try_now_button())

    # 3 main feature
    def tap_remove_objects_button(self):
        super().click(HomePageLocators.remove_objects_button())

    def tap_remove_background_button(self):
        super().click(HomePageLocators.remove_background_button())

    def tap_start_editing_button(self):
        super().click(HomePageLocators.start_editing_button())

    # secondery action scrollview
    def tap_ai_enhance_button(self):
        super().click(HomePageLocators.ai_enhance_button())

    def tap_ai_replace_button(self):
        super().click(HomePageLocators.ai_replace_button())

    def tap_collage_button(self):
        super().click(HomePageLocators.collage_button())

    def tap_design_button(self):
        super().click(HomePageLocators.design_button())

    def tap_filter_button(self):
        super().click(HomePageLocators.filter_button())

    def tap_blur_button(self):
        super().click(HomePageLocators.blur_button())

    def tap_brushes_button(self):
        super().click(HomePageLocators.brushes_button())

    def tap_crop_button(self):
        super().click(HomePageLocators.crop_button())

    def tap_sticker_button(self):
        super().click(HomePageLocators.sticker_button())

    def tap_ai_filters_button(self):
        super().click(HomePageLocators.ai_filters_button())

    def tap_ai_expand_button(self):
        super().click(HomePageLocators.ai_expand_button())

    def tap_ai_generate_button(self):
        super().click(HomePageLocators.ai_generate_button())

    def tap_frame_button(self):
        super().click(HomePageLocators.frame_button())

    def tap_adjust_button(self):
        super().click(HomePageLocators.adjust_button())

    def tap_texture_button(self):
        super().click(HomePageLocators.texture_button())

    def tap_reshape_button(self):
        super().click(HomePageLocators.reshape_button())

    def tap_text_button(self):
        super().click(HomePageLocators.text_button())

    def tap_basic_edit_button(self):
        super().click(HomePageLocators.basic_edit_button())

    # banners 
    def tap_remove_background_banner(self):
        super().click(HomePageLocators.remove_background_banner())

    def tap_remove_objects_banner(self):
        super().click(HomePageLocators.remove_objects_banner())

    def tap_ai_enhance_banner(self):
        super().click(HomePageLocators.ai_enhance_banner())

    def tap_ai_expand_banner(self):
        super().click(HomePageLocators.ai_expand_banner())

    def tap_basic_edit_banner(self):
        super().click(HomePageLocators.basic_edit_banner())

    def tap_ai_generate_banner(self):
        super().click(HomePageLocators.ai_generate_banner())

    def tap_ai_filters_banner(self):
        super().click(HomePageLocators.ai_filters_banner())

    def tap_ai_fill_banner(self):
        super().click(HomePageLocators.ai_fill_banner())

    # narv bar 
    def tap_home_tab(self):
        super().click(HomePageLocators.home_tab())

    def tap_template_tab(self):
        super().click(HomePageLocators.template_tab())

    def tap_ai_filters_tab(self):
        super().click(HomePageLocators.ai_filters_tab())

    def tap_ai_generate_tab(self):
        super().click(HomePageLocators.ai_generate_tab())

    