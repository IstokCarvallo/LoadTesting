"""
Cliente de Recepciones.
"""

from models import ApiResponse, ConsultaRequest
from config import config
from .base_client import BaseClient


class RecepcionesClient(BaseClient):
    """Cliente para consultar el endpoint de Recepciones."""

    def consultar(self, access_token: str,
        consulta: ConsultaRequest,) -> ApiResponse:
        
        return self.post(
            endpoint=config.endpoints.recepciones,
            json={
                "clienteId": consulta.cliente_id,
                "fechaProceso": consulta.fecha_proceso,
            },
            headers=self.create_headers(access_token),
        )