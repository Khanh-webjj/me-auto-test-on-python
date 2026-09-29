from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
RESOURCE_PATH = PROJECT_ROOT / "resources"


class ResourceManager:

    @staticmethod
    def _get_resource_path(directory: str, file_name: str) -> str:
        resource_path = RESOURCE_PATH / directory / file_name

        if not resource_path.exists():
            raise FileNotFoundError(
                f"Resource file '{file_name}' not found at {resource_path}"
            )

        if not resource_path.is_file():
            raise ValueError(
                f"Resource path '{resource_path}' is not a file"
            )
        return str(resource_path.resolve())

    @classmethod
    def get_app(cls, filename: str) -> str:
        return cls._get_resource_path("apps", filename)

    @classmethod
    def get_image(cls, filename: str) -> str:
        return cls._get_resource_path("images", filename)