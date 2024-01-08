"""
Tabuladores v4, CRUD (create, read, update, and delete)
"""
from typing import Any

from sqlalchemy.orm import Session

from lib.exceptions import MyIsDeletedError, MyNotExistsError
from perseo.v4.puestos.crud import get_puesto

from ...core.tabuladores.models import Tabulador


def get_tabuladores(
    database: Session,
    puesto_id: int = None,
) -> Any:
    """Consultar los tabuladores activos"""
    consulta = database.query(Tabulador)
    if puesto_id is not None:
        puesto = get_puesto(database, puesto_id)
        consulta = consulta.filter_by(puesto_id=puesto.id)
    return consulta.filter_by(estatus="A").order_by(Tabulador.id)


def get_tabulador(database: Session, tabulador_id: int) -> Tabulador:
    """Consultar un tabulador por su id"""
    tabulador = database.query(Tabulador).get(tabulador_id)
    if tabulador is None:
        raise MyNotExistsError("No existe ese tabulador")
    if tabulador.estatus != "A":
        raise MyIsDeletedError("No es activo ese tabulador, está eliminado")
    return tabulador
