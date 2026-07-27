"""
Cliente de Recepciones.
"""

from models import ConsultaRequest
from config import config
from .base_client import BaseClient


class RecepcionesClient(BaseClient):
    def consultar(
        self,
        access_token: str,
        consulta: ConsultaRequest,
    ) -> dict:

        response = self.post(
            endpoint=config.endpoints.recepciones,
            json={
                "clienteId": consulta.cliente_id,
                "fechaProceso": consulta.fecha_proceso,
            },
            headers=self.create_headers(access_token),
        )

        return response.json()