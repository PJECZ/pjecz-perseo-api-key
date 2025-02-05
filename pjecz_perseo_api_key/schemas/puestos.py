"""
Puestos v4, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict

from ..dependencies.schemas_base import OneBaseOut


class PuestoOut(BaseModel):
    """Esquema para entregar puestos"""

    id: int
    clave: str
    descripcion: str
    model_config = ConfigDict(from_attributes=True)


class OnePuestoOut(OneBaseOut):
    """Esquema para entregar un puesto"""

    data: PuestoOut | None = None
