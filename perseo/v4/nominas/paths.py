"""
Nominas v4, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_nomina, get_nominas
from .schemas import NominaOut, OneNominaOut

nominas = APIRouter(prefix="/v4/nominas", tags=["nominas"])


@nominas.get("", response_model=CustomPage[NominaOut])
async def paginado_nominas(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    curp: str = None,
    rfc: str = None,
):
    """Paginado de nominas"""
    if current_user.permissions.get("NOMINAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_nominas(
            database=database,
            curp=curp,
            rfc=rfc,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@nominas.get("/{nomina_id}", response_model=OneNominaOut)
async def detalle_nomina(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    nomina_id: int,
):
    """Detalle de una nomina a partir de su id"""
    if current_user.permissions.get("NOMINAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        nomina = get_nomina(database, nomina_id)
    except MyAnyError as error:
        return OneNominaOut(success=False, message=str(error))
    return OneNominaOut.model_validate(nomina)
