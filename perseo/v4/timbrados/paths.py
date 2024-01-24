"""
Timbrados v4, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_timbrados, get_timbrado
from .schemas import TimbradoOut, OneTimbradoOut

timbrados = APIRouter(prefix="/v4/timbrados", tags=["timbrados"])


@timbrados.get("", response_model=CustomPage[TimbradoOut])
async def paginado_timbrados(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    curp: str = None,
    rfc: str = None,
):
    """Paginado de timbrados"""
    if current_user.permissions.get("TIMBRADOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_timbrados(
            database=database,
            curp=curp,
            rfc=rfc,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@timbrados.get("/{timbrado_id}", response_model=OneTimbradoOut)
async def detalle_timbrado(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    timbrado_id: int,
):
    """Detalle de un timbrado a partir de su id"""
    if current_user.permissions.get("TIMBRADOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        timbrado = get_timbrado(database, timbrado_id)
    except MyAnyError as error:
        return OneTimbradoOut(success=False, message=str(error))
    return OneTimbradoOut.model_validate(timbrado)
