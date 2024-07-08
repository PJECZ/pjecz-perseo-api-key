"""
Personas v4, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.database import Session, get_db
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_page import CustomPage

from ...core.permisos.models import Permiso
from ..usuarios.authentications import UsuarioInDB, get_current_active_user
from .crud import get_persona_with_rfc, get_personas
from .schemas import OnePersonaOut, PersonaOut

personas = APIRouter(prefix="/v4/personas", tags=["personas"])


@personas.get("", response_model=CustomPage[PersonaOut])
async def paginado_personas(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    tabulador_id: int = None,
    rfc: str = None,
    nombres: str = None,
    apellido_primero: str = None,
    apellido_segundo: str = None,
    curp: str = None,
):
    """Paginado de personas"""
    if current_user.permissions.get("PERSONAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        resultados = get_personas(
            database=database,
            tabulador_id=tabulador_id,
            rfc=rfc,
            nombres=nombres,
            apellido_primero=apellido_primero,
            apellido_segundo=apellido_segundo,
            curp=curp,
        )
    except MyAnyError as error:
        return CustomPage(success=False, message=str(error))
    return paginate(resultados)


@personas.get("/{persona_rfc}", response_model=OnePersonaOut)
async def detalle_persona(
    current_user: Annotated[UsuarioInDB, Depends(get_current_active_user)],
    database: Annotated[Session, Depends(get_db)],
    persona_rfc: str,
):
    """Detalle de una persona a partir de su RFC"""
    if current_user.permissions.get("PERSONAS", 0) < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        persona = get_persona_with_rfc(database, persona_rfc)
    except MyAnyError as error:
        return OnePersonaOut(success=False, message=str(error))
    return OnePersonaOut.model_validate(persona)
