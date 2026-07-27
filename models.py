"""
Modelos de configuración de la aplicación.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ApiConfig:
    host: str


@dataclass(frozen=True)
class AuthenticationConfig:
    login: str
    refresh: str
    refresh_margin_seconds: int


@dataclass(frozen=True)
class EndpointConfig:
    recepciones: str
    despachos: str


@dataclass(frozen=True)
class DatasetConfig:
    usuarios: str
    consultas: str


@dataclass(frozen=True)
class LoggingConfig:
    level: str
    folder: str


@dataclass(frozen=True)
class AppConfig:
    api: ApiConfig
    authentication: AuthenticationConfig
    endpoints: EndpointConfig
    datasets: DatasetConfig
    logging: LoggingConfig