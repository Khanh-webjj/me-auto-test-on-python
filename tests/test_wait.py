from unittest.mock import Mock

from core.util.wait import Wait


def test_wait_uses_configured_explicit_timeout():
    wait = Wait(Mock())

    assert wait.timeout == 10


def test_clickable_wait_returns_clickable_element():
    locator = ("id", "continue")
    element = Mock()
    element.is_displayed.return_value = True
    element.is_enabled.return_value = True
    driver = Mock()
    driver.find_element.return_value = element

    result = Wait(driver, timeout=0.1).clickable(locator)

    assert result is element
