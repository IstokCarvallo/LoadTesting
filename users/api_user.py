"""
Usuario virtual de Locust.
"""

from locust import User, between
from scenarios.movimientos import MovimientoScenario


class ApiUser(User):
    wait_time = between(1, 3)    
    tasks = [MovimientoScenario]