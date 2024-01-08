"""
Puestos v4, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_puestos, get_puesto_with_clave
from .schemas import PuestoOut, OnePuestoOut

puestos = APIRouter(prefix="/v4/puestos", tags=["puestos"])


@puestos.get("", response_model=CustomPage[PuestoOut])
async def paginado_puestos(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
):
    """Paginado de puestos"""
    if current_user.permissions.get("PUESTOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_puestos(database)
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@puestos.get("/{puesto_clave}", response_model=OnePuestoOut)
async def detalle_puesto(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    puesto_clave: str,
):
    """Detalle de un puesto a partir de su clave"""
    if current_user.permissions.get("PUESTOS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        puesto = get_puesto_with_clave(database, puesto_clave)
    except MyAnyError as error:
        return OnePuestoOut(success=False, message=str(error))
    return OnePuestoOut.model_validate(puesto)
