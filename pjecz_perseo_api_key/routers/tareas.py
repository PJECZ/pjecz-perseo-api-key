"""
Tareas
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from ..dependencies.authentications import UsuarioInDB, get_current_active_user
from ..dependencies.database import Session, get_db
from ..dependencies.fastapi_pagination_custom_page import CustomPage
from ..dependencies.safe_string import safe_email
from ..models.permisos import Permiso
from ..models.tareas import Tarea
from ..models.usuarios import Usuario
from ..schemas.tareas import TareaOut

tareas = APIRouter(prefix="/api/v5/tareas", tags=["usuarios"])


@tareas.get("", response_model=CustomPage[TareaOut])
async def paginado_tareas(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    email: str = None,
):
    """Paginado de tareas"""
    if current_user.permissions.get("TAREAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    consulta = database.query(Tarea)
    if email is not None:
        try:
            email = safe_email(email)
        except ValueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No es válido el e-mail")
        consulta = consulta.join(Usuario).filter(Usuario.email == email).filter(Usuario.estatus == "A")
    return paginate(consulta.filter(Tarea.estatus == "A").order_by(Tarea.id.desc()))
