"""
Eventos globales de Locust.
"""

from locust import events

from metrics import metrics
from metrics.metrics_reporter import MetricsReporter


@events.quitting.add_listener
def on_quitting(environment, **kwargs):

    reporter = MetricsReporter(metrics)

    reporter.print()