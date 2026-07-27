"""
Cliente de autenticación.
"""

from datetime import datetime
from config import config
from models import LoginResponse, TokenInfo
from .base_client import BaseClient


class AuthClient(BaseClient):
    def login(
        self,
        username: str,
        password: str,
    ) -> LoginResponse:

        response = self.post(
            config.authentication.login,
            {
                "username": username,
                "password": password,
            },
        )

        data = response.json()["data"]

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

    def refresh(self, refresh_token: str,) -> TokenInfo:
        response = self.post(
            config.authentication.refresh,
            {
                "refreshToken": refresh_token,
            },
        )

        data = response.json()["data"]

        return TokenInfo(
            access_token=data["accessToken"],
            refresh_token=data["refreshToken"],
            expiration=datetime.fromisoformat(
                data["accessTokenExpiration"].replace("Z", "+00:00")
            ),
        )