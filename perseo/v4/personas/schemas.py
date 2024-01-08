"""
Personas v4, esquemas de pydantic
"""
from datetime import date

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class PersonaOut(BaseModel):
    """Esquema para entregar personas"""

    id: int | None = None
    tabulador_id: int | None = None
    rfc: str | None = None
    nombres: str | None = None
    apellido_primero: str | None = None
    apellido_segundo: str | None = None
    curp: str | None = None
    num_empleado: int | None = None
    ingreso_gobierno_fecha: date | None = None
    ingreso_pj_fecha: date | None = None
    nacimiento_fecha: date | None = None
    codigo_postal_fiscal: int | None = None
    seguridad_social: str | None = None
    modelo: int | None = None
    nombre_completo: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OnePersonaOut(PersonaOut, OneBaseOut):
    """Esquema para entregar una persona"""
