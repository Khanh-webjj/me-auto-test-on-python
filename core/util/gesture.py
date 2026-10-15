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

    def long_press_component(self, element, duration=1000):
        action = ActionChains(self.driver)
        pointer = PointerInput("touch", "finger")
        action.w3c_actions = ActionBuilder(self.driver, mouse=pointer)
        action.w3c_actions.pointer_action.move_to(element)
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

    def scroll_inside_element(self, element_locator, direction = "left", duration = 1000, distance_ratio = 0.7):
        element = self.driver.find_element(*element_locator)
        rect = element.rect

        x = rect["x"]
        y = rect["y"]
        width = rect["width"]
        height = rect["height"]

        center_x = x + width//2
        center_y = y + height//2

        horizontal_distance = int(width * distance_ratio)
        vertical_distance = int(height * distance_ratio)

        if direction == "left":
            start_x = x + width - width * 0.1
            end_x = start_x - horizontal_distance
            start_y = end_y = center_y
        elif direction == "right":
            start_x = x + width * 0.1
            end_x = start_x + horizontal_distance
            start_y = end_y = center_y
        elif direction == "up":
            start_y = y  + height - height * 0.1
            end_y = start_y - vertical_distance
            start_x = end_x = center_x
        elif direction == "down":
            start_y = y + height * 0.1
            end_y = start_y + vertical_distance
            start_x = end_x = center_x
        else: 
            raise ValueError("direction must be 'left', 'right', 'up' or 'down'")

        self.scroll(int(start_x), int(start_y), int(end_x), int(end_y), duration)


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