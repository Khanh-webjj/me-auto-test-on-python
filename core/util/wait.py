from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.util.config import Config

class Wait:
    def __init__(self, driver, timeout=None):
        self.driver = driver

        if timeout is None:
            timeout = Config().get("wait", "timeout")

        self.timeout = timeout

        self._wait = WebDriverWait(driver, timeout)

    def presence(self, locator):
        return self._wait.until(
            EC.presence_of_element_located(locator)
        )

    def visible(self, locator):
        return self._wait.until(
            EC.visibility_of_element_located(locator)
        )

    def invisible(self, locator):
        return self._wait.until(
            EC.invisibility_of_element_located(locator)
        )

    def exists(self, locator):
        try:
            self.presence(locator)
            return True
        except TimeoutException:
            return False