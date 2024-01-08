"""
Puestos v4, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_clave

from ...core.puestos.models import Puesto


def get_puestos(database: Session) -> Any:
    """Consultar los puestos activos"""
    return database.query(Puesto).filter_by(estatus="A").order_by(Puesto.clave)


def get_puesto(database: Session, puesto_id: int) -> Puesto:
    """Consultar un puesto por su id"""
    puesto = database.query(Puesto).get(puesto_id)
    if puesto is None:
        raise MyNotExistsError("No existe ese puesto")
    if puesto.estatus != "A":
        raise MyIsDeletedError("No es activo ese puesto, está eliminado")
    return puesto


def get_puesto_with_clave(database: Session, puesto_clave: str) -> Puesto:
    """Consultar un puesto por su clave"""
    try:
        clave = safe_clave(puesto_clave)
    except ValueError as error:
        raise MyNotValidParamError(str(error)) from error
    puesto = database.query(Puesto).filter_by(clave=clave).first()
    if puesto is None:
        raise MyNotExistsError("No existe ese puesto")
    if puesto.estatus != "A":
        raise MyIsDeletedError("No es activo ese puesto, está eliminado")
    return puesto
