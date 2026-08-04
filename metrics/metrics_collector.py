from collections import defaultdict

from metrics.metric_record import MetricRecord


class MetricsCollector:

    def __init__(self) -> None:
        self._records: list[MetricRecord] = []

    def add(
        self,
        endpoint: str,
        elapsed_ms: float,
        status_code: int,
        success: bool,
    ) -> None:

        self._records.append(
            MetricRecord(
                endpoint=endpoint,
                elapsed_ms=elapsed_ms,
                status_code=status_code,
                success=success,
            )
        )

    @property
    def records(self) -> list[MetricRecord]:
        return self._records

    def endpoints(self) -> list[str]:
        return sorted(
            {
                r.endpoint
                for r in self._records
            }
        )

    def by_endpoint(
        self,
        endpoint: str,
    ) -> list[MetricRecord]:

        return [
            r
            for r in self._records
            if r.endpoint == endpoint
        ]

    def total_requests(self) -> int:
        return len(self._records)

    def total_errors(self) -> int:
        return sum(
            not r.success
            for r in self._records
        )