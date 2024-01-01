"""
Distritos v4, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError, MyNotValidParamError
from lib.safe_string import safe_clave

from ...core.distritos.models import Distrito


def get_distritos(database: Session) -> Any:
    """Consultar los distritos activos"""
    return database.query(Distrito).filter_by(estatus="A").order_by(Distrito.clave)


def get_distrito(database: Session, distrito_id: int) -> Distrito:
    """Consultar un distrito por su id"""
    distrito = database.query(Distrito).get(distrito_id)
    if distrito is None:
        raise MyNotExistsError("No existe ese distrito")
    if distrito.estatus != "A":
        raise MyIsDeletedError("No es activo ese distrito, está eliminado")
    return distrito


def get_distrito_with_clave(database: Session, distrito_clave: str) -> Distrito:
    """Consultar un distrito por su clave"""
    try:
        clave = safe_clave(distrito_clave)
    except ValueError as error:
        raise MyNotValidParamError(str(error)) from error
    distrito = database.query(Distrito).filter_by(clave=clave).first()
    if distrito is None:
        raise MyNotExistsError("No existe ese distrito")
    if distrito.estatus != "A":
        raise MyIsDeletedError("No es activo ese distrito, está eliminado")
    return distrito
