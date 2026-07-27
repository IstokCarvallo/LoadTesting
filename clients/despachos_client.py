"""
Cliente de Despachos.
"""

from models import ApiResponse, ConsultaRequest
from config import config
from .base_client import BaseClient


class DespachosClient(BaseClient):
    """Cliente para consultar el endpoint de Despachos."""

    def consultar(self, access_token: str,
        consulta: ConsultaRequest,) -> ApiResponse:

        return self.post(
            endpoint=config.endpoints.despachos,
            json={
                "clienteId": consulta.cliente_id,
                "fechaProceso": consulta.fecha_proceso,
            },
            headers=self.create_headers(access_token),
        )