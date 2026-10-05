from pages.base_page import BasePage
from components.panels.brush_image_panel.brush_image_panel_locators import BrushPanelLocators
from components.panels.brush_panel.brush_panel import BrushMainPanel


class PhotoEditorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.brush_panel = BrushMainPanel(driver)

    def is_brush_panel_displayed(self):
        return self.is_displayed(BrushPanelLocators.root())