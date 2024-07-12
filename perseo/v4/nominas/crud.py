"""
Nominas v4, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError

from ...core.nominas.models import Nomina
from ..personas.crud import get_persona_with_curp, get_persona_with_rfc


def get_nominas(
    database: Session,
    curp: str = None,
    rfc: str = None,
) -> Any:
    """Consultar las nominas activos"""
    consulta = database.query(Nomina)
    if curp is not None:
        persona = get_persona_with_curp(database, curp)
        consulta = consulta.filter_by(persona_id=persona.id)
    if rfc is not None:
        persona = get_persona_with_rfc(database, rfc)
        consulta = consulta.filter_by(persona_id=persona.id)
    return consulta.filter(Nomina.estatus == "A").order_by(Nomina.id.desc())


def get_nomina(database: Session, nomina_id: int) -> Nomina:
    """Consultar una nomina por su id"""
    nomina = database.query(Nomina).get(nomina_id)
    if nomina is None:
        raise MyNotExistsError("No existe ese nomina")
    if nomina.estatus != "A":
        raise MyIsDeletedError("No es activo ese nomina, está eliminado")
    return nomina
