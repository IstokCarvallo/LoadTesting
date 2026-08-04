from time import perf_counter

from models import ApiResponse
from services.load_runner import LoadRunner
from metrics import metrics, MetricsReporter


class LocustAdapter:
    def __init__(self):
        self._runner = LoadRunner()
        self._metrics = metrics

        self._last_login_count = 0
        self._last_refresh_count = 0

    def _collect_auth_metrics(self) -> None:
        auth = self._runner.auth

        if auth.login_count > self._last_login_count:
            self._metrics.add(
                endpoint="/Auth/Login",
                elapsed_ms=auth.last_login_elapsed_ms,
                status_code=auth.last_login_status_code,
                success=auth.last_login_status_code == 200,
            )

            self._last_login_count = auth.login_count

        if auth.refresh_count > self._last_refresh_count:
            self._metrics.add(
                endpoint="/Auth/Refresh",
                elapsed_ms=auth.last_refresh_elapsed_ms,
                status_code=auth.last_refresh_status_code,
                success=auth.last_refresh_status_code == 200,
            )

            self._last_refresh_count = auth.refresh_count


    def ejecutar_recepcion(self) -> ApiResponse:
        respuesta = self._runner.ejecutar_recepcion()

        self._collect_auth_metrics()

        self._metrics.add(
            endpoint="/Recepciones",
            elapsed_ms=respuesta.elapsed_ms,
            status_code=respuesta.status_code,
            success=respuesta.success,
        )

        return respuesta

    def ejecutar_despacho(self) -> ApiResponse:        
        respuesta = self._runner.ejecutar_despacho()

        self._collect_auth_metrics()

        self._metrics.add(
            endpoint="/Despachos",
            elapsed_ms=respuesta.elapsed_ms,
            status_code=respuesta.status_code,
            success=respuesta.success,
        )

        return respuesta

    def summary(self):
        return self._metrics.summary()

    def print_report(self) -> None:
        reporter = MetricsReporter(self._metrics)

        reporter.print()