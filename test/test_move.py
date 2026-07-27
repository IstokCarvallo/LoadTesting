from clients.recepciones_client import RecepcionesClient
from clients.despachos_client import DespachosClient

from models import ConsultaRequest
from services.auth_manager import AuthManager

import jwt

USERNAME = "Admin"
PASSWORD = "Admin123456*"


try:

    print("Login...")

    auth = AuthManager()

    auth.login(USERNAME, PASSWORD)

    print("OK")

    token = auth.get_access_token()
    print(token)
    print("Token obtenido")

    consulta = ConsultaRequest(
        cliente_id=3,
        fecha_proceso="2026-02-16"
    )

    claims = jwt.decode(
        token,
        options={"verify_signature": False}
    )

    print(claims)

    print("Consultando Recepciones...")

    recepciones = RecepcionesClient()

    respuesta = recepciones.consultar(
        token,
        consulta
    )

    print("Respuesta Recepciones")

    print(respuesta)

    print("Consultando Despachos...")

    despachos = DespachosClient()

    respuesta = despachos.consultar(
        token,
        consulta
    )

    print("Respuesta Despachos")

    print(respuesta)

except Exception as ex:

    print(type(ex).__name__)
    print(ex)