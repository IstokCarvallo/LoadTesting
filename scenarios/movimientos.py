"""
Escenarios de carga.
"""

from locust import TaskSet, task
from adapters.locust_adapter import LocustAdapter


class MovimientoScenario(TaskSet):
    def on_start(self):
        self.adapter = LocustAdapter()

    @task(3)
    def recepciones(self):
        respuesta = self.adapter.ejecutar_recepcion()

        if not respuesta.success:
            print(
                f"Recepción {respuesta.status_code} - {respuesta.error}"
            )

    @task(1)
    def despachos(self):
        respuesta = self.adapter.ejecutar_despacho()

        if not respuesta.success:
            print(
                f"Despacho {respuesta.status_code} - {respuesta.error}"
            )