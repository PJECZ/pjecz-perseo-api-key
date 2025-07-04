"""
Autoridades v4, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict

from ..dependencies.schemas_base import OneBaseOut


class AutoridadOut(BaseModel):
    """Esquema para entregar autoridades"""

    clave: str
    distrito_clave: str
    distrito_nombre: str
    distrito_nombre_corto: str
    descripcion: str
    descripcion_corta: str
    es_extinto: bool
    model_config = ConfigDict(from_attributes=True)


class OneAutoridadOut(OneBaseOut):
    """Esquema para entregar un autoridad"""

    data: AutoridadOut | None = None
