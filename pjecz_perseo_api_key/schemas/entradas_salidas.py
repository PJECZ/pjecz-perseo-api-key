"""
Entradas-Salidas v4, esquemas de pydantic
"""

from pydantic import BaseModel, ConfigDict

from ..dependencies.schemas_base import OneBaseOut


class EntradaSalidaOut(BaseModel):
    """Esquema para entregar entradas-salidas"""

    id: int
    usuario_email: str
    tipo: str
    direccion_ip: str
    model_config = ConfigDict(from_attributes=True)


class OneEntradaSalidaOut(OneBaseOut):
    """Esquema para entregar una entrada-salida"""

    data: EntradaSalidaOut | None = None
