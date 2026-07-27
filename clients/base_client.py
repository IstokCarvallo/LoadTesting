"""
Cliente HTTP base.
"""

from __future__ import annotations
from typing import Any
import requests
from config import config
from models import ApiResponse


class BaseClient:
    """Cliente HTTP base para consumir la API."""

    DEFAULT_TIMEOUT = 30

    def __init__(self) -> None:
        self._session = requests.Session()
        self._base_url = config.api.host.rstrip("/")

    def create_headers(self, access_token: str) -> dict[str, str]:
        """Construye los encabezados estándar para la API."""
        return {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def post(self, endpoint: str,
        json: dict[str, Any],
        headers: dict[str, str] | None = None,) -> ApiResponse:

        try:
            response = self._session.post(
                f"{self._base_url}{endpoint}",
                json=json,
                headers=headers,
                timeout=self.DEFAULT_TIMEOUT,
            )

            body: dict[str, Any] = {}

            if response.content:
                try:
                    body = response.json()
                except ValueError:
                    body = {"raw": response.text}

            return ApiResponse(
                success=response.ok,
                status_code=response.status_code,
                elapsed_ms=response.elapsed.total_seconds() * 1000,
                body=body,
                error=None if response.ok else body.get("message"),
            )

        except requests.RequestException as ex:
            return ApiResponse(
                success=False,
                status_code=0,
                elapsed_ms=0,
                body={},
                error=str(ex),
            )

    def get(self, endpoint: str,
        headers: dict[str, str] | None = None,) -> ApiResponse:

        try:
            response = self._session.get(
                f"{self._base_url}{endpoint}",
                headers=headers,
                timeout=self.DEFAULT_TIMEOUT,
            )

            body: dict[str, Any] = {}

            if response.content:
                try:
                    body = response.json()
                except ValueError:
                    body = {"raw": response.text}

            return ApiResponse(
                success=response.ok,
                status_code=response.status_code,
                elapsed_ms=response.elapsed.total_seconds() * 1000,
                body=body,
                error=None if response.ok else body.get("message"),
            )

        except requests.RequestException as ex:
            return ApiResponse(
                success=False,
                status_code=0,
                elapsed_ms=0,
                body={},
                error=str(ex),
            )