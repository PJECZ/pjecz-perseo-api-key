"""
Tareas v4, esquemas de pydantic
"""
from pydantic import BaseModel, ConfigDict

from lib.schemas_base import OneBaseOut


class TareaOut(BaseModel):
    """Esquema para entregar tareas"""

    id: int | None = None
    usuario_id: int | None = None
    usuario_email: str | None = None
    comando: str | None = None
    mensaje: str | None = None
    ha_terminado: bool | None = None
    model_config = ConfigDict(from_attributes=True)


class OneTareaOut(TareaOut, OneBaseOut):
    """Esquema para entregar un tarea"""
