"""
Cliente HTTP base.
"""

from __future__ import annotations
from typing import Any
import requests
from config import config


class BaseClient:
    """Cliente HTTP base para consumir la API."""

    DEFAULT_TIMEOUT = 30

    def __init__(self) -> None:
        self._session = requests.Session()
        self._base_url = config.api.host.rstrip("/")

    def create_headers(self, access_token: str) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def post(self, endpoint: str,
        json: dict[str, Any],
        headers: dict[str, str] | None = None,
    ) -> requests.Response:

        response = self._session.post(
            f"{self._base_url}{endpoint}",
            json=json,
            headers=headers,
            timeout=self.DEFAULT_TIMEOUT,
        )

        response.raise_for_status()

        return response

    def get(self, endpoint: str,
        headers: dict[str, str] | None = None,
    ) -> requests.Response:

        response = self._session.get(
            f"{self._base_url}{endpoint}",
            headers=headers,
            timeout=self.DEFAULT_TIMEOUT,
        )

        response.raise_for_status()

        return response