from dataclasses import dataclass

@dataclass(frozen=True)
class ApiConfig:
    host: str


@dataclass(frozen=True)
class AuthenticationConfig:
    endpoint: str


@dataclass(frozen=True)
class EndpointConfig:
    recepcion: str
    despacho: str


@dataclass(frozen=True)
class DatasetConfig:
    usuarios: str
    consultas: str


@dataclass(frozen=True)
class AppConfig:
    api: ApiConfig
    authentication: AuthenticationConfig
    endpoints: EndpointConfig
    datasets: DatasetConfig