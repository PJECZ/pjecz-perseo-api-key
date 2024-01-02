"""
Autoridades v4, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class AutoridadOut(BaseModel):
    """Esquema para entregar autoridades"""

    id: int | None = None
    distrito_id: int | None = None
    distrito_clave: str | None = None
    clave: str | None = None
    descripcion: str | None = None
    descripcion_corta: str | None = None
    es_extinto: bool | None = None
    model_config = ConfigDict(from_attributes=True)


class OneAutoridadOut(AutoridadOut, OneBaseOut):
    """Esquema para entregar un autoridad"""
