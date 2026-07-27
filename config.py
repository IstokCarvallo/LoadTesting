"""
Carga de configuración desde config.yaml.
"""

from pathlib import Path

import yaml

from models import (
    ApiConfig,
    AppConfig,
    AuthenticationConfig,
    DatasetConfig,
    EndpointConfig,
    LoggingConfig,
)


class ConfigLoader:
    """Carga y valida la configuración de la aplicación."""

    BASE_PATH = Path(__file__).resolve().parent
    CONFIG_FILE = BASE_PATH / "config.yaml"

    @classmethod
    def load(cls) -> AppConfig:

        with cls.CONFIG_FILE.open(encoding="utf-8") as file:
            config = yaml.safe_load(file)

        return AppConfig(
            api=ApiConfig(**config["api"]),
            authentication=AuthenticationConfig(**config["authentication"]),
            endpoints=EndpointConfig(**config["endpoints"]),
            datasets=DatasetConfig(**config["datasets"]),
            logging=LoggingConfig(**config["logging"]),
        )


config = ConfigLoader.load()