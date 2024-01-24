"""
Nominas v4, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class NominaOut(BaseModel):
    """Esquema para entregar nominas"""

    id: int | None = None
    persona_id: int | None = None
    persona_curp: str | None = None
    persona_rfc: str | None = None
    tipo: str | None = None
    timbrado_id: int | None = None
    model_config = ConfigDict(from_attributes=True)


class OneNominaOut(NominaOut, OneBaseOut):
    """Esquema para entregar una nomina"""
