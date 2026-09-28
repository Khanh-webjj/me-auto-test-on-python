from pathlib import Path
import yaml


PROJECT_ROOT = Path(__file__).parent.parent.parent
CONFIG_PATH = PROJECT_ROOT / "config.yaml"

class Config:
    def __init__(self):
        self.config = self.load_config()

    @staticmethod
    def load_config():
        if not CONFIG_PATH.exists():
            raise FileNotFoundError(
                f"Config file not found at {CONFIG_PATH}"
            )

        with open(CONFIG_PATH, "r") as f:
            return yaml.safe_load(f)

        if not config:
            raise ValueError("Config file is empty or invalid")

        return config

    def get(self, *keys):
        value = self.config

        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                raise KeyError(f"Key '{key}' not found in config")
        
        return value

    @property
    def appium_server_url(self):
        return self.get("appium", "server_url")

    @property
    def platform_name(self):
        return self.get("android", "platform_name")

    @property
    def automation_name(self):
        return self.get("android", "automation_name")

    @property
    def device_name(self):
        return self.get("android", "device_name")

    @property
    def app_package(self):
        return self.get("android", "app_package")

    @property
    def no_reset(self):
        return self.get("android", "no_reset")

    @property
    def auto_grant_permissions(self):
        return self.get("android", "auto_grant_permissions")

    @property
    def explicit_wait(self):
        return self.get("timeouts", "explicit")