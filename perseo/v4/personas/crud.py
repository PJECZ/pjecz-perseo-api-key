"""
Personas v4, CRUD (create, read, update, and delete)
"""

from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_curp, safe_rfc, safe_string
from perseo.v4.tabuladores.crud import get_tabulador

from ...core.personas.models import Persona


def get_personas(
    database: Session,
    tabulador_id: int = None,
    rfc: str = None,
    nombres: str = None,
    apellido_primero: str = None,
    apellido_segundo: str = None,
    curp: str = None,
) -> Any:
    """Consultar las personas activos"""
    consulta = database.query(Persona)
    if tabulador_id is not None:
        tabulador = get_tabulador(database, tabulador_id)
        consulta = consulta.filter_by(tabulador_id=tabulador.id)
    if rfc is not None:
        try:
            rfc = safe_rfc(rfc, search_fragment=True)
        except ValueError as error:
            raise MyNotValidParamError(str(error)) from error
        consulta = consulta.filter(Persona.rfc.contains(rfc))
    if nombres is not None:
        nombres = safe_string(nombres, save_enie=True)
        if nombres != "":
            consulta = consulta.filter(Persona.nombres.contains(nombres))
    if apellido_primero is not None:
        apellido_primero = safe_string(apellido_primero, save_enie=True)
        if apellido_primero != "":
            consulta = consulta.filter(Persona.apellido_primero.contains(apellido_primero))
    if apellido_segundo is not None:
        apellido_segundo = safe_string(apellido_segundo, save_enie=True)
        if apellido_segundo != "":
            consulta = consulta.filter(Persona.apellido_segundo.contains(apellido_segundo))
    if curp is not None:
        try:
            curp = safe_curp(curp, search_fragment=True)
        except ValueError as error:
            raise MyNotValidParamError(str(error)) from error
        consulta = consulta.filter(Persona.curp.contains(curp))
    return consulta.filter(Persona.estatus == "A").order_by(Persona.id)


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


def get_persona_with_curp(database: Session, persona_curp: str) -> Persona:
    """Consultar una persona por su CURP (porque el CURP no es único, se obtiene la primera coincidencia con estatus A)"""
    try:
        curp = safe_curp(persona_curp)
    except ValueError as error:
        raise MyNotValidParamError(str(error)) from error
    persona = database.query(Persona).filter_by(curp=curp).filter_by(estatus="A").first()
    if persona is None:
        raise MyNotExistsError("No existe ese persona")
    return persona
