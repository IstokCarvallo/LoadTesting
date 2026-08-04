"""
Administrador de autenticación.
"""

from datetime import datetime, timedelta, timezone
from clients.auth_client import AuthClient
from config import config
from models import AuthResult, RefreshResult, LoginResponse, TokenInfo


class AuthManager:
    """Administra el ciclo de vida del Access Token."""    


    def __init__(self) -> None:
        self._client = AuthClient()
        self._login: LoginResponse | None = None
        self._token: TokenInfo | None = None

        self._last_login_elapsed_ms: float = 0
        self._last_refresh_elapsed_ms: float = 0
        self._login_count = 0
        self._refresh_count = 0


    def login(self, username: str, password: str,) -> None:

        result: AuthResult = self._client.login(
            username=username,
            password=password,
        )

        self._login = result.login
        self._token = result.login.token

        self._last_login_elapsed_ms = result.elapsed_ms
        self._last_login_status_code = result.status_code

        self._login_count += 1


    def get_access_token(self) -> str:
        if self._token is None:
            raise RuntimeError("Debe autenticarse antes de solicitar un token.")

        margin = timedelta(seconds=config.authentication.refresh_margin_seconds)

        if datetime.now(timezone.utc) >= self._token.expiration - margin:
            result: RefreshResult = self._client.refresh(
                self._token.refresh_token,
            )

            self._token = result.token

            self._last_refresh_elapsed_ms = result.elapsed_ms
            self._last_refresh_status_code = result.status_code

            self._refresh_count += 1

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


    @property
    def user_id(self) -> int:
        if self._login is None:
            return 0

        return self._login.user_id


    @property
    def token_expiration(self):
        if self._token is None:
            return None

        return self._token.expiration


    @property
    def last_login_elapsed_ms(self) -> float:
        return self._last_login_elapsed_ms


    @property
    def last_login_status_code(self) -> int:
        return self._last_login_status_code


    @property
    def last_refresh_elapsed_ms(self) -> float:
        return self._last_refresh_elapsed_ms


    @property
    def last_refresh_status_code(self) -> int:
        return self._last_refresh_status_code

    @property
    def login_count(self) -> int:
        return self._login_count


    @property
    def refresh_count(self) -> int:
        return self._refresh_count