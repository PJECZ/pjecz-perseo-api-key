"""
Tabuladores v4, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_tabuladores, get_tabulador
from .schemas import TabuladorOut, OneTabuladorOut

tabuladores = APIRouter(prefix="/v4/tabuladores", tags=["tabuladores"])


@tabuladores.get("", response_model=CustomPage[TabuladorOut])
async def paginado_tabuladores(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    puesto_id: int = None,
):
    """Paginado de tabuladores"""
    if current_user.permissions.get("TABULADORES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_tabuladores(
            database=database,
            puesto_id=puesto_id,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@tabuladores.get("/{tabulador_id}", response_model=OneTabuladorOut)
async def detalle_tabulador(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    tabulador_id: int,
):
    """Detalle de una tabulador a partir de su id"""
    if current_user.permissions.get("TABULADORES", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        tabulador = get_tabulador(database, tabulador_id)
    except MyAnyError as error:
        return OneTabuladorOut(success=False, message=str(error))
    return OneTabuladorOut.model_validate(tabulador)
