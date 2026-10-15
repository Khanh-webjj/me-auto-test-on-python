from core.util.wait import Wait
from core.util.gesture import Gesture


class BaseComponent:
    def __init__(self, driver):
        self.driver = driver
        self.wait = Wait(driver)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.wait.clickable(locator).click()

    def send_keys(self, locator, text):
        element = self.wait.visible(locator)
        element.clear()
        element.send_keys(text)

    def long_press(self, locator, duration=1000):
        element = self.wait.visible(locator)
        gesture = Gesture(self.driver)
        gesture.long_press_component(element, duration)


    def get_text(self, locator):
        return self.wait.visible(locator).text

    def is_displayed(self, locator):
        return self.wait.exists(locator)

    def get_attribute(self, locator, attribute):
        element = self.wait.presence(locator)
        return element.get_attribute(attribute)
