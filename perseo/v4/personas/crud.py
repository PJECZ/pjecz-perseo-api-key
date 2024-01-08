"""
Personas v4, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_rfc
from perseo.v4.tabuladores.crud import get_tabulador

from ...core.personas.models import Persona


def get_personas(
    database: Session,
    tabulador_id: int = None,
) -> Any:
    """Consultar las personas activos"""
    consulta = database.query(Persona)
    if tabulador_id is not None:
        tabulador = get_tabulador(database, tabulador_id)
        consulta = consulta.filter_by(tabulador_id=tabulador.id)
    return consulta.filter_by(estatus="A").order_by(Persona.id)


def get_persona(database: Session, persona_id: int) -> Persona:
    """Consultar una persona por su id"""
    persona = database.query(Persona).get(persona_id)
    if persona is None:
        raise MyNotExistsError("No existe ese persona")
    if persona.estatus != "A":
        raise MyIsDeletedError("No es activo ese persona, está eliminado")
    return persona


def get_persona_with_rfc(database: Session, persona_rfc: str) -> Persona:
    """Consultar una persona por su RFC"""
    try:
        rfc = safe_rfc(persona_rfc)
    except ValueError as error:
        raise MyNotValidParamError(str(error)) from error
    persona = database.query(Persona).filter_by(rfc=rfc).first()
    if persona is None:
        raise MyNotExistsError("No existe ese persona")
    if persona.estatus != "A":
        raise MyIsDeletedError("No es activa ese persona, está eliminada")
    return persona
