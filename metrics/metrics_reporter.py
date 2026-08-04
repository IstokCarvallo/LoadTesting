"""
Generador de reportes de métricas.
"""

from statistics import mean

from metrics.metrics_collector import MetricsCollector


class MetricsReporter:
    def __init__(
        self,
        collector: MetricsCollector,
    ) -> None:

        self._collector = collector

    def generate(self) -> dict:
        report: dict = {}

        for endpoint in self._collector.endpoints():
            records = self._collector.by_endpoint(endpoint)
            elapsed = [r.elapsed_ms for r in records]
            success = sum(r.success for r in records)

            report[endpoint] = {
                "requests": len(records),
                "success": success,
                "errors": len(records) - success,
                "min_ms": min(elapsed),
                "max_ms": max(elapsed),
                "avg_ms": round(mean(elapsed), 2,),
            }

        return report

    def print(self) -> None:
        report = self.generate()

        print()
        print("=" * 60)
        print("LOAD TEST SUMMARY")
        print("=" * 60)

        for endpoint, data in report.items():

            print()
            print(endpoint)
            print("-" * len(endpoint))

            print(f"Requests : {data['requests']}")
            print(f"Success  : {data['success']}")
            print(f"Errors   : {data['errors']}")
            print(f"Min (ms) : {data['min_ms']:.2f}")
            print(f"Avg (ms) : {data['avg_ms']:.2f}")
            print(f"Max (ms) : {data['max_ms']:.2f}")

        print()
        print("=" * 60)