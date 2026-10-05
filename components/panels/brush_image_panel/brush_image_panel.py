from components.panels.brush_panel.brush_panel_locators import BrushPanelLocators
from components.panels.panel import Panel  


class BrushMainPanel(Panel):
    def tap_done_button(self):
        self.click(BrushPanelLocators.done_button())

    def tap_duplicate_button(self):
        self.click(BrushPanelLocators.duplicate_button())

    def tap_delete_button(self):
        self.click(BrushPanelLocators.delete_button()) 

    def tap_layer_up_button(self):
        self.click(BrushPanelLocators.layer_up_button())

    def tap_layer_down_button(self):
        self.click(BrushPanelLocators.layer_down_button())

    def tap_layer_top_button(self):
        self.click(BrushPanelLocators.layer_top_button())  

    def tap_layer_bottom_button(self):
        self.click(BrushPanelLocators.layer_bottom_button())

    def tap_flip_vertical_button(self):
        self.click(BrushPanelLocators.flip_vertical_button())

    def tap_flip_horizontal_button(self):
        self.click(BrushPanelLocators.flip_horizontal_button())

    def tap_edit_button(self):
        self.click(BrushPanelLocators.edit_button())

    def tap_opacity_button(self):
        self.click(BrushPanelLocators.opacity_button())

    def tap_adjust_button(self):
        self.click(BrushPanelLocators.adjust_button())

    def tap_outline_button(self):
        self.click(BrushPanelLocators.outline_button())

    def tap_shadow_button(self):
        self.click(BrushPanelLocators.shadow_button())

    def tap_reflection_button(self):
        self.click(BrushPanelLocators.reflection_button())
