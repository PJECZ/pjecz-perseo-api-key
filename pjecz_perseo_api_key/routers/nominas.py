"""
Nominas
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate

from ..dependencies.authentications import UsuarioInDB, get_current_active_user
from ..dependencies.database import Session, get_db
from ..dependencies.fastapi_pagination_custom_page import CustomPage
from ..dependencies.safe_string import safe_curp, safe_rfc
from ..models.nominas import Nomina
from ..models.permisos import Permiso
from ..models.personas import Persona
from ..schemas.nominas import NominaOut

nominas = APIRouter(prefix="/api/v5/nominas", tags=["nominas"])


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
    consulta = database.query(Nomina)
    if curp is not None:
        try:
            curp = safe_curp(curp, search_fragment=True)
        except ValueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No es válido el CURP")
        consulta = consulta.join(Persona).filter(Persona.curp == curp).filter(Persona.estatus == "A")
    elif rfc is not None:
        try:
            rfc = safe_rfc(rfc)
        except ValueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No es válido el RFC")
        consulta = consulta.join(Persona).filter(Persona.rfc == rfc).filter(Persona.estatus == "A")
    return paginate(consulta.filter(Nomina.estatus == "A").order_by(Nomina.id.desc()))
