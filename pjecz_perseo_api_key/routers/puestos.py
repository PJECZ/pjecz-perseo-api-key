"""
Puestos
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from ..dependencies.authentications import UsuarioInDB, get_current_active_user
from ..dependencies.database import Session, get_db
from ..dependencies.fastapi_pagination_custom_page import CustomPage
from ..models.permisos import Permiso
from ..models.puestos import Puesto
from ..schemas.puestos import PuestoOut

puestos = APIRouter(prefix="/api/v5/puestos", tags=["puestos"])


@puestos.get("", response_model=CustomPage[PuestoOut])
async def paginado_puestos(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Paginado de puestos"""
    if current_user.permissions.get("PUESTOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    return paginate(database.query(Puesto).filter_by(estatus="A").order_by(Puesto.clave))
