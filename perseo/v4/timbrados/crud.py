"""
Timbrados v4, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.nominas.models import Nomina
from ...core.timbrados.models import Timbrado
from ..personas.crud import get_persona_with_curp, get_persona_with_rfc


def get_timbrados(
    database: Session,
    curp: str = None,
    rfc: str = None,
) -> Any:
    """Consultar los timbrados activos"""
    consulta = database.query(Timbrado)
    if curp is not None or rfc is not None:
        consulta = consulta.join(Nomina)
    if curp is not None:
        persona = get_persona_with_curp(database, curp)
        consulta = consulta.filter(Nomina.persona_id == persona.id)
    if rfc is not None:
        persona = get_persona_with_rfc(database, rfc)
        consulta = consulta.filter(Nomina.persona_id == persona.id)
    return consulta.filter_by(estatus="A").order_by(Timbrado.id.desc())


def get_timbrado(database: Session, timbrado_id: int) -> Timbrado:
    """Consultar un timbrado por su id"""
    timbrado = database.query(Timbrado).get(timbrado_id)
    if timbrado is None:
        raise MyNotExistsError("No existe ese timbrado")
    if timbrado.estatus != "A":
        raise MyIsDeletedError("No es activo ese timbrado, está eliminado")
    return timbrado
