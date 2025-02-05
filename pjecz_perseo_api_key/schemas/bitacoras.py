"""
Bitacoras v4, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict

from ..dependencies.schemas_base import OneBaseOut


class BitacoraOut(BaseModel):
    """Esquema para entregar bitácoras"""

    id: int
    modulo_nombre: str
    usuario_email: str
    descripcion: str
    url: str
    model_config = ConfigDict(from_attributes=True)


class OneBitacoraOut(OneBaseOut):
    """Esquema para entregar una bitácora"""

    data: BitacoraOut | None = None
