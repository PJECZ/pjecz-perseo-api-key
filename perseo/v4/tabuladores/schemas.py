"""
Tabuladores v4, esquemas de pydantic
"""
from datetime import date

from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class TabuladorOut(BaseModel):
    """Esquema para entregar tabuladores"""

    id: int | None = None
    puesto_id: int | None = None
    puesto_clave: str | None = None
    puesto_descripcion: str | None = None
    modelo: int | None = None
    nivel: int | None = None
    quinquenio: int | None = None
    fecha: date | None = None
    sueldo_base: float | None = None
    incentivo: float | None = None
    monedero: float | None = None
    rec_cul_dep: float | None = None
    sobresueldo: float | None = None
    rec_dep_cul_gravado: float | None = None
    rec_dep_cul_excento: float | None = None
    ayuda_transp: float | None = None
    monto_quinquenio: float | None = None
    total_percepciones: float | None = None
    salario_diario: float | None = None
    prima_vacacional_mensual: float | None = None
    aguinaldo_mensual: float | None = None
    prima_vacacional_mensual_adicional: float | None = None
    total_percepciones_integrado: float | None = None
    salario_diario_integrado: float | None = None
    model_config = ConfigDict(from_attributes=True)


class OneTabuladorOut(TabuladorOut, OneBaseOut):
    """Esquema para entregar un tabulador"""
