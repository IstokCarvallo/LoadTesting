from dataclasses import dataclass


@dataclass(slots=True)
class MetricRecord:
    endpoint: str
    elapsed_ms: float
    status_code: int
    success: bool