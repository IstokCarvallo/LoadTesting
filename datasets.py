from __future__ import annotations

import csv
from itertools import cycle
from pathlib import Path

from config import config
from models import ConsultaRequest, Usuario


BASE_PATH = Path(__file__).resolve().parent


class DatasetProvider:
    """
    Administra los datasets utilizados por las pruebas.
    """
    REQUIRED_USERS_COLUMNS = {"Username", "Password"}
    REQUIRED_CONSULTAS_COLUMNS = {"ClienteId", "FechaProceso"}

    def __init__(self):
        self._usuarios = self._load_users()
        self._consultas = self._load_consultas()

        self._usuarios_cycle = cycle(self._usuarios)
        self._consultas_cycle = cycle(self._consultas)

    def _load_users(self) -> list[Usuario]:
        path = BASE_PATH / config.datasets.usuarios
        self._validate_file(path)

        usuarios: list[Usuario] = []

        with path.open(newline="", encoding="utf-8",) as file:
            reader = csv.DictReader(file)

            self._validate_columns(
                reader.fieldnames,
                self.REQUIRED_USERS_COLUMNS,
                path.name,
            )

            for index, row in enumerate(reader, start=2):
                try:
                    usuarios.append(
                        Usuario(
                            username=row["Username"].strip(),
                            password=row["Password"].strip(),
                        )
                    )

                except Exception as ex:
                    raise ValueError(f"Error en {path.name}, línea {index}: {ex}") from ex

        if not usuarios:
            raise ValueError(f"{path.name} no contiene registros.")

        return usuarios

    def _load_consultas(self) -> list[ConsultaRequest]:
        path = BASE_PATH / config.datasets.consultas
        self._validate_file(path)

        consultas: list[ConsultaRequest] = []

        with path.open(newline="", encoding="utf-8",) as file:

            reader = csv.DictReader(file)

            self._validate_columns(
                reader.fieldnames,
                self.REQUIRED_CONSULTAS_COLUMNS,
                path.name,
            )

            for index, row in enumerate(reader, start=2):
                try:
                    consultas.append(
                        ConsultaRequest(
                            cliente_id=int(row["ClienteId"]),
                            fecha_proceso=row["FechaProceso"].strip(),
                        )
                    )

                except Exception as ex:
                    raise ValueError(
                        f"Error en {path.name}, línea {index}: {ex}"
                    ) from ex

        if not consultas:
            raise ValueError(f"{path.name} no contiene registros.")

        return consultas

    @staticmethod
    def _validate_file(path: Path) -> None:
        if not path.exists():
            raise FileNotFoundError(f"No existe el archivo: {path}")

    @staticmethod
    def _validate_columns(
        fieldnames: list[str] | None,
        required: set[str],
        file_name: str,) -> None:

        if fieldnames is None:
            raise ValueError(f"{file_name} no posee encabezados.")

        missing = required - set(fieldnames)

        if missing:
            raise ValueError(
                f"{file_name} no contiene las columnas: {', '.join(sorted(missing))}"
            )

    def next_user(self) -> Usuario:
        """Obtiene el siguiente usuario del dataset."""
        return next(self._usuarios_cycle)

    def next_consulta(self) -> ConsultaRequest:
        """Obtiene la siguiente consulta del dataset."""
        return next(self._consultas_cycle)