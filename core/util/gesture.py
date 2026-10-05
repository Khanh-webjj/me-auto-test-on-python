from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class Gesture:
    def __init__(self, driver):
        self.driver = driver

    def tap(self, x, y):
        action = ActionChains(self.driver)
        pointer = PointerInput("touch", "finger")
        action.w3c_actions = ActionBuilder(self.driver, mouse=pointer)
        action.w3c_actions.pointer_action.move_to_location(x, y)
        action.w3c_actions.pointer_action.click()
        action.perform()

    def double_tap(self, x, y):
        action = ActionChains(self.driver)
        pointer = PointerInput("touch", "finger")
        action.w3c_actions = ActionBuilder(self.driver, mouse=pointer)
        action.w3c_actions.pointer_action.move_to_location(x, y)
        action.w3c_actions.pointer_action.click()
        action.w3c_actions.pointer_action.pause(0.1)  # Short pause between taps
        action.w3c_actions.pointer_action.click()
        action.perform()

    def long_press(self, x, y, duration=1000):
        action = ActionChains(self.driver)
        pointer = PointerInput("touch", "finger")
        action.w3c_actions = ActionBuilder(self.driver, mouse=pointer)
        action.w3c_actions.pointer_action.move_to_location(x, y)
        action.w3c_actions.pointer_action.pointer_down()
        action.w3c_actions.pointer_action.pause(duration / 1000)  # Convert milliseconds to seconds
        action.w3c_actions.pointer_action.pointer_up()
        action.perform()

    def swipe(self, start_x, start_y, end_x, end_y, duration=1000):
        action = ActionChains(self.driver)
        pointer = PointerInput("touch", "finger")
        action.w3c_actions = ActionBuilder(self.driver, mouse=pointer)
        action.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        action.w3c_actions.pointer_action.pointer_down()
        action.w3c_actions.pointer_action.pause(duration / 1000)  # Convert milliseconds to seconds
        action.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        action.w3c_actions.pointer_action.pointer_up()
        action.perform()

    def scroll(self, start_x, start_y, end_x, end_y, duration=1000):
        self.swipe(start_x, start_y, end_x, end_y, duration)

    def drag_and_drop(self, start_x, start_y, end_x, end_y, duration=1000):
        action = ActionChains(self.driver)
        pointer = PointerInput("touch", "finger")
        action.w3c_actions = ActionBuilder(self.driver, mouse=pointer)
        action.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        action.w3c_actions.pointer_action.pointer_down()
        action.w3c_actions.pointer_action.pause(duration / 1000)  # Convert milliseconds to seconds
        action.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        action.w3c_actions.pointer_action.pointer_up()
        action.perform()