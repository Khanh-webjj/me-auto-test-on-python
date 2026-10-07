from photo_editor_main_panel.photo_editor_main_panel_locators import PhotoEditorMainPanelLocators
from core.util.gesture import Gesture

from components.panels.panel import Panel

class PhotoEditorMainPanel(Panel):
    def __init__(self, driver):
        self.driver = driver
        self.gesture = Gesture(self.driver)

    def is_displayed(self):
        return self.driver.is_displayed(PhotoEditorMainPanelLocators.root())   

    # top bar button
    def tap_back_button(self):
        self.driver.click(PhotoEditorMainPanelLocators.back_button())

    def tap_undo_button(self):
        self.driver.click(PhotoEditorMainPanelLocators.undo_button())

    def tap_redo_button(self):
        self.driver.click(PhotoEditorMainPanelLocators.redo_button())

    def tap_compare_button(self):
        self.driver.click(PhotoEditorMainPanelLocators.compare_button())

    def long_press_compare_button(self):
        compare_button = self.driver.find_element(PhotoEditorMainPanelLocators.compare_button())
        action = ActionChains(self.driver)
        action.click_and_hold(compare_button).pause(2).perform()

    def tap_save_button(self):
        self.driver.click(PhotoEditorMainPanelLocators.save_button())

    # main panel button
    def tap_layer_button(self):
        self.driver.click(PhotoEditorMainPanelLocators.layer_button())

    def tap_insert_button(self):
        self.driver.click(PhotoEditorMainPanelLocators.insert_button())

    def tap_crop_button(self):
        if self.driver.is_displayed(PhotoEditorMainPanelLocators.crop_button()):
            self.driver.click(PhotoEditorMainPanelLocators.crop_button())
        else:
            raise Exception("Crop button is not displayed.")

    def tap_cleanup_button(self):
        if self.driver.is_displayed(PhotoEditorMainPanelLocators.cleanup_button()):
            self.driver.click(PhotoEditorMainPanelLocators.cleanup_button())
        else:
            raise Exception("Cleanup button is not displayed.")

    def tap_reshape_button(self):
        if self.driver.is_displayed(PhotoEditorMainPanelLocators.reshape_button()):
            self.driver.click(PhotoEditorMainPanelLocators.reshape_button())
        else:
            raise Exception("Reshape button is not displayed.")

    def tap_ai_enhance_button(self):
        if self.driver.is_displayed(PhotoEditorMainPanelLocators.ai_enhance_button()):
            self.driver.click(PhotoEditorMainPanelLocators.ai_enhance_button())
        else:
            raise Exception("AI Enhance button is not displayed.")

    def tap_ai_expand_button(self):
        if self.driver.is_displayed(PhotoEditorMainPanelLocators.ai_expand_button()):
            self.driver.click(PhotoEditorMainPanelLocators.ai_expand_button())
        else:
            raise Exception("AI Expand button is not displayed.")   

    def tap_adjust_button(self):
        if self.driver.is_displayed(PhotoEditorMainPanelLocators.adjust_button()):
            self.driver.click(PhotoEditorMainPanelLocators.adjust_button())
        else:
            raise Exception("Adjust button is not displayed.")  

    def tap_partial_button(self):
        if self.driver.is_displayed(PhotoEditorMainPanelLocators.partial_button()):
            self.driver.click(PhotoEditorMainPanelLocators.partial_button())
        else:
            raise Exception("Partial button is not displayed.") 

    def tap_hsl_button(self):
        if self.driver.is_displayed(PhotoEditorMainPanelLocators.hsl_button()):
            self.driver.click(PhotoEditorMainPanelLocators.hsl_button())
        else:
            raise Exception("HSL button is not displayed.")

    def tap_wb_button(self):
        if self.driver.is_displayed(PhotoEditorMainPanelLocators.wb_button()):
            self.driver.click(PhotoEditorMainPanelLocators.wb_button())
        else:
            raise Exception("WB button is not displayed.")

    def tap_filter_button(self):
        if self.driver.is_displayed(PhotoEditorMainPanelLocators.filter_button()):
            self.driver.click(PhotoEditorMainPanelLocators.filter_button())
        else:
            raise Exception("Filter button is not displayed.")

    def tap_blur_button(self):
        if self.driver.is_displayed(PhotoEditorMainPanelLocators.blur_button()):
            self.driver.click(PhotoEditorMainPanelLocators.blur_button())
        else:
            raise Exception("Blur button is not displayed.")

    def tap_texture_button(self):
        if self.driver.is_displayed(PhotoEditorMainPanelLocators.texture_button()):
            self.driver.click(PhotoEditorMainPanelLocators.texture_button())
        else:
            raise Exception("Texture button is not displayed.")

    def tap_frame_button(self):
        if self.driver.is_displayed(PhotoEditorMainPanelLocators.frame_button()):
            self.driver.click(PhotoEditorMainPanelLocators.frame_button())
        else:
            raise Exception("Frame button is not displayed.")

    def tap_brushes_button(self):
        if self.driver.is_displayed(PhotoEditorMainPanelLocators.brushes_button()):
            self.driver.click(PhotoEditorMainPanelLocators.brushes_button())
        else:
            raise Exception("Brushes button is not displayed.")
    
    def scroll_to_button(self, button_locator, max_swipes = 10):
        
        view = self.driver.find_element(PhotoEditorMainPanelLocators.horizontal_scroll_view())

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
        
    