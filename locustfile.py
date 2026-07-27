from locust import HttpUser

from config import config
from logger import get_logger

logger = get_logger(__name__)

logger.info("Configuración cargada correctamente.")
logger.info("Host: %s", config.api.host)


class ApiUser(HttpUser):
    host = config.api.host