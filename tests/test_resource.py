from pathlib import Path

from core.util.resource import ResourceManager


def test_get_app_resource_path():
    app_filename = "BSVba_3.3.15_382_202608241527.apk"
    app_path = ResourceManager.get_app(app_filename)

    assert Path(app_path).exists()
    assert Path(app_path).is_file()