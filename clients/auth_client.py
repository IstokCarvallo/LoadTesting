"""
Cliente de autenticación.
"""

from datetime import datetime
from config import config
from models import ApiResponse, AuthResult, RefreshResult, LoginResponse, TokenInfo
from .base_client import BaseClient


class AuthClient(BaseClient):
    """Cliente para autenticación contra la API."""

    def login(self, username: str, password: str,) -> AuthResult:
        response: ApiResponse = self.post(
            config.authentication.login,
            {
                "username": username,
                "password": password,
            },
        )

        if not response.success:
            raise RuntimeError(
                response.error
                or f"Error de autenticación ({response.status_code})"
            )

        data = response.body["data"]

        login = LoginResponse(
            user_id=data["userId"],
            username=data["username"],
            roles=data["roles"],
            token=TokenInfo(
                access_token=data["accessToken"],
                refresh_token=data["refreshToken"],
                expiration=datetime.fromisoformat(
                    data["accessTokenExpiration"].replace("Z", "+00:00")
                ),
            ),
        )

        return AuthResult(
                login=login,
                elapsed_ms=response.elapsed_ms,
                status_code=response.status_code,
            )

    def refresh(self, refresh_token: str,) -> RefreshResult:

        response: ApiResponse = self.post(
            config.authentication.refresh,
            {
                "refreshToken": refresh_token,
            },
        )

        if not response.success:
            raise RuntimeError(
                response.error
                or f"Error al refrescar token ({response.status_code})"
            )

        data = response.body["data"]

        token = TokenInfo(
            access_token=data["accessToken"],
            refresh_token=data["refreshToken"],
            expiration=datetime.fromisoformat(
                data["accessTokenExpiration"].replace("Z", "+00:00")
            ),
        )

        return RefreshResult(
            token=token,
            elapsed_ms=response.elapsed_ms,
            status_code=response.status_code,
        )