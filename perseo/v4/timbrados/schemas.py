"""
Timbrados v4, esquemas de pydantic
"""
from datetime import date

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class TimbradoOut(BaseModel):
    """Esquema para entregar timbrados"""

    id: int | None = None
    nomina_id: int | None = None
    nomina_fecha_pago: date | None = None
    nomina_tipo: str | None = None
    persona_rfc: str | None = None
    persona_curp: str | None = None
    estado: str | None = None
    archivo_pdf: str | None = None
    url_pdf: str | None = None
    archivo_xml: str | None = None
    url_xml: str | None = None
    model_config = ConfigDict(from_attributes=True)


class OneTimbradoOut(TimbradoOut, OneBaseOut):
    """Esquema para entregar un timbrado"""
