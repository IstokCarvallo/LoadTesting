"""
Orquestador de las pruebas de carga.
"""

from datasets import DatasetProvider
from services.auth_manager import AuthManager

from clients.recepciones_client import RecepcionesClient
from clients.despachos_client import DespachosClient

from models import ApiResponse


class LoadRunner:
    @property
    def auth(self) -> AuthManager:
        return self._auth

    
    def __init__(self) -> None:
        self._datasets = DatasetProvider()
        self._auth = AuthManager()
        self._recepciones = RecepcionesClient()
        self._despachos = DespachosClient()

        self._authenticated = False


    def _authenticate(self) -> None:
        if self._authenticated:
            return

        usuario = self._datasets.next_user()

        self._auth.login(
            username=usuario.username,
            password=usuario.password,
        )

        self._authenticated = True


    def ejecutar_recepcion(self) -> ApiResponse:
        self._authenticate()
        consulta = self._datasets.next_consulta()

        return self._recepciones.consultar(
            access_token=self._auth.get_access_token(),
            consulta=consulta,
        )


    def ejecutar_despacho(self) -> ApiResponse:
        self._authenticate()
        consulta = self._datasets.next_consulta()

        return self._despachos.consultar(
            access_token=self._auth.get_access_token(),
            consulta=consulta,
        )
