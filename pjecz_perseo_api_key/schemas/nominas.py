"""
Nominas v4, esquemas de pydantic
"""

from datetime import date

from pydantic import BaseModel, ConfigDict

from ..dependencies.schemas_base import OneBaseOut


class NominaOut(BaseModel):
    """Esquema para entregar nominas"""

    id: int
    persona_id: int
    persona_curp: str
    persona_rfc: str
    fecha_pago: date
    tipo: str
    timbrado_id: int
    model_config = ConfigDict(from_attributes=True)


class OneNominaOut(OneBaseOut):
    """Esquema para entregar una nomina"""

    data: NominaOut | None = None
