from core.util.config import Config

def test_config():
    config = Config()

    assert config.appium_server_url == "http://127.0.0.1:4723"
    assert config.platform_name == "Android"
    assert config.automation_name == "UiAutomator2"
    assert config.app_package == "com.duygiangdg.magiceraser"