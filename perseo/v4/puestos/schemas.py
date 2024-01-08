"""
Puestos v4, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class PuestoOut(BaseModel):
    """Esquema para entregar puestos"""

    id: int | None = None
    clave: str | None = None
    descripcion: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OnePuestoOut(PuestoOut, OneBaseOut):
    """Esquema para entregar un puesto"""
