"""
Administrador de autenticación.
"""

from datetime import datetime, timedelta, timezone
from clients.auth_client import AuthClient
from config import config
from models import LoginResponse, TokenInfo


class AuthManager:
    def __init__(self) -> None:
        self._client = AuthClient()
        self._login: LoginResponse | None = None
        self._token: TokenInfo | None = None

    def login(self, username: str, password: str,) -> None:
        self._login = self._client.login(
            username,
            password,
        )

        self._token = self._login.token

    def get_access_token(self) -> str:
        if self._token is None:
            raise RuntimeError("Debe autenticarse antes de solicitar un token.")

        margin = timedelta(seconds=config.authentication.refresh_margin_seconds)

        if datetime.now(timezone.utc) >= self._token.expiration - margin:
            self._token = self._client.refresh(self._token.refresh_token)

        return self._token.access_token

    @property
    def username(self) -> str:
        if self._login is None:
            return ""

        return self._login.username

    @property
    def roles(self) -> list[str]:
        if self._login is None:
            return []

        return self._login.roles