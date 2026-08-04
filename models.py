"""
Modelos de configuración de la aplicación.
"""
from datetime import datetime
from dataclasses import dataclass,  field
from typing import Any


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

@dataclass
class TokenInfo:
    """Información de autenticación."""

    access_token: str
    refresh_token: str
    expiration: datetime


@dataclass
class LoginResponse:
    """Respuesta de autenticación."""

    user_id: int
    username: str
    roles: list[str]
    token: TokenInfo


@dataclass(frozen=True)
class ConsultaRequest:
    """Solicitud de consulta de movimientos."""

    cliente_id: int
    fecha_proceso: str


@dataclass(frozen=True)
class Usuario:
    """Solicitud de usuarios para API."""
    username: str
    password: str


@dataclass(frozen=True)
class ApiResponse:
    """Respuesta estándar de cualquier llamada a la API."""

    success: bool
    status_code: int
    elapsed_ms: float
    body: dict[str, Any] = field(default_factory=dict)
    error: str | None = None


@dataclass(frozen=True)
class AuthResult:
    """Resultado de una autenticación."""

    login: LoginResponse
    elapsed_ms: float
    status_code: int


@dataclass(frozen=True)
class RefreshResult:
    """Resultado de una renovación de token."""

    token: TokenInfo
    elapsed_ms: float
    status_code: int