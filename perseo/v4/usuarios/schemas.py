"""
Usuarios v4, esquemas de pydantic
"""
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class UsuarioOut(BaseModel):
    """Esquema para entregar usuarios"""

    id: int | None = None
    autoridad_id: int | None = None
    autoridad_clave: str | None = None
    nombres: str | None = None
    apellido_primero: str | None = None
    apellido_segundo: str | None = None
    curp: str | None = None
    puesto: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneUsuarioOut(UsuarioOut, OneBaseOut):
    """Esquema para entregar un usuario"""


class UsuarioInDB(UsuarioOut):
    """Usuario en base de datos"""

    username: str
    permissions: dict
    hashed_password: str
    disabled: bool
    api_key: str
    api_key_expiracion: datetime
