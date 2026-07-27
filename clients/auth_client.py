"""
Cliente de autenticación.
"""

from datetime import datetime
from config import config
from models import ApiResponse, LoginResponse, TokenInfo
from .base_client import BaseClient


class AuthClient(BaseClient):
    """Cliente para autenticación contra la API."""

    def login(
        self,
        username: str,
        password: str,
    ) -> LoginResponse:

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

        return LoginResponse(
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

    def refresh(
        self,
        refresh_token: str,
    ) -> TokenInfo:

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

        return TokenInfo(
            access_token=data["accessToken"],
            refresh_token=data["refreshToken"],
            expiration=datetime.fromisoformat(
                data["accessTokenExpiration"].replace("Z", "+00:00")
            ),
        )