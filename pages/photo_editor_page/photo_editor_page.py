from pages.photo_editor_page.photo_edito_page_locators import PhotoEditorPageLocators
from core.util.gesture import Gesture

from components.panels.panel import Panel

class PhotoEditorMainPanel(Panel):
    def __init__(self, driver):
        super().__init__(driver)

    def is_displayed(self):
        return super().is_displayed(PhotoEditorPageLocators.root())   

    # top bar button
    def tap_back_button(self):
        super().click(PhotoEditorPageLocators.back_button())

    def tap_undo_button(self):
        super().click(PhotoEditorPageLocators.undo_button())

    def tap_redo_button(self):
        super().click(PhotoEditorPageLocators.redo_button())

    def tap_compare_button(self):
        super().click(PhotoEditorPageLocators.compare_button())

    def long_press_compare_button(self):
        compare_button = super().find_element(PhotoEditorPageLocators.compare_button())
        super().long_press(compare_button)

    def tap_save_button(self):
        super().click(PhotoEditorPageLocators.save_button())

    # main panel button
    def tap_layer_button(self):
        super().click(PhotoEditorPageLocators.layer_button())

    def tap_insert_button(self):
        super().click(PhotoEditorPageLocators.insert_button())

    def tap_crop_button(self):
        if super().is_displayed(PhotoEditorPageLocators.crop_button()):
            super().click(PhotoEditorPageLocators.crop_button())
        else:
            raise Exception("Crop button is not displayed.")

    def tap_cleanup_button(self):
        if super().is_displayed(PhotoEditorPageLocators.cleanup_button()):
            super().click(PhotoEditorPageLocators.cleanup_button())
        else:
            raise Exception("Cleanup button is not displayed.")

    def tap_reshape_button(self):
        if super().is_displayed(PhotoEditorPageLocators.reshape_button()):
            super().click(PhotoEditorPageLocators.reshape_button())
        else:
            raise Exception("Reshape button is not displayed.")

    def tap_ai_enhance_button(self):
        if super().is_displayed(PhotoEditorPageLocators.ai_enhance_button()):
            super().click(PhotoEditorPageLocators.ai_enhance_button())
        else:
            raise Exception("AI Enhance button is not displayed.")

    def tap_ai_expand_button(self):
        if super().is_displayed(PhotoEditorPageLocators.ai_expand_button()):
            super().click(PhotoEditorPageLocators.ai_expand_button())
        else:
            raise Exception("AI Expand button is not displayed.")   

    def tap_adjust_button(self):
        if super().is_displayed(PhotoEditorPageLocators.adjust_button()):
            super().click(PhotoEditorPageLocators.adjust_button())
        else:
            raise Exception("Adjust button is not displayed.")  

    def tap_partial_button(self):
        if super().is_displayed(PhotoEditorPageLocators.partial_button()):
            super().click(PhotoEditorPageLocators.partial_button())
        else:
            raise Exception("Partial button is not displayed.") 

    def tap_hsl_button(self):
        if super().is_displayed(PhotoEditorPageLocators.hsl_button()):
            super().click(PhotoEditorPageLocators.hsl_button())
        else:
            raise Exception("HSL button is not displayed.")

    def tap_wb_button(self):
        if super().is_displayed(PhotoEditorPageLocators.wb_button()):
            super().click(PhotoEditorPageLocators.wb_button())
        else:
            raise Exception("WB button is not displayed.")

    def tap_filter_button(self):
        if super().is_displayed(PhotoEditorPageLocators.filter_button()):
            super().click(PhotoEditorPageLocators.filter_button())
        else:
            raise Exception("Filter button is not displayed.")

    def tap_blur_button(self):
        if super().is_displayed(PhotoEditorPageLocators.blur_button()):
            super().click(PhotoEditorPageLocators.blur_button())
        else:
            raise Exception("Blur button is not displayed.")

    def tap_texture_button(self):
        if super().is_displayed(PhotoEditorPageLocators.texture_button()):
            super().click(PhotoEditorPageLocators.texture_button())
        else:
            raise Exception("Texture button is not displayed.")

    def tap_frame_button(self):
        if super().is_displayed(PhotoEditorPageLocators.frame_button()):
            super().click(PhotoEditorPageLocators.frame_button())
        else:
            raise Exception("Frame button is not displayed.")

    def tap_brushes_button(self):
        if super().is_displayed(PhotoEditorPageLocators.brushes_button()):
            super().click(PhotoEditorPageLocators.brushes_button())
        else:
            raise Exception("Brushes button is not displayed.")
    
    def scroll_to_button(self, button_locator, max_swipes = 10):
        
        view = self.driver.find_element(PhotoEditorPageLocators.horizontal_scroll_view())

        rect = view.rect

        center_y = rect['y'] + rect['height'] / 2
        start_x = rect['x'] + rect['width'] * 0.8
        end_x = rect['x'] + rect['width'] * 0.2

        for _ in range(max_swipes):
            button = self.driver.find_element(button_locator)

            if button:
                return button

            self.gesture.swipe(start_x, center_y, end_x, center_y, duration=500)

        raise Exception(f"Button with locator {button_locator} not found after {max_swipes} swipes.")
        
    