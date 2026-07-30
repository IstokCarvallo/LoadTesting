from time import perf_counter

from models import ApiResponse
from services.load_runner import LoadRunner


class LocustAdapter:
    def __init__(self):
        self._runner = LoadRunner()

    def ejecutar_recepcion(self) -> ApiResponse:
        return self._runner.ejecutar_recepcion()

    def ejecutar_despacho(self) -> ApiResponse:
        return self._runner.ejecutar_despacho()