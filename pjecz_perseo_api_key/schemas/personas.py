"""
Personas v4, esquemas de pydantic
"""

from datetime import date

from pydantic import BaseModel, ConfigDict

from ..dependencies.schemas_base import OneBaseOut


class PersonaOut(BaseModel):
    """Esquema para entregar personas"""

    id: int
    tabulador_id: int
    rfc: str
    nombres: str
    apellido_primero: str
    apellido_segundo: str
    curp: str
    num_empleado: int
    ingreso_gobierno_fecha: date
    ingreso_pj_fecha: date
    nacimiento_fecha: date
    codigo_postal_fiscal: int
    seguridad_social: str
    modelo: int
    nombre_completo: str
    model_config = ConfigDict(from_attributes=True)


class OnePersonaOut(OneBaseOut):
    """Esquema para entregar una persona"""

    data: PersonaOut | None = None
