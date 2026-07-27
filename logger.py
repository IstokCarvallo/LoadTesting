"""
Configuración del sistema de logging.
"""

import logging
from pathlib import Path

from config import config
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

LOG_FOLDER = Path(config.logging.folder)
LOG_FOLDER.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_FOLDER / f"loadtesting_{timestamp}.log"


logging.basicConfig(
    level=getattr(logging, config.logging.level.upper()),
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)


def get_logger(name: str) -> logging.Logger:
    """Obtiene un logger configurado."""

    return logging.getLogger(name)