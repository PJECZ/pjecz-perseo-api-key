"""
Timbrados, modelos
"""
from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Timbrado(Base, UniversalMixin):
    """Timbrado"""

    ESTADOS = {
        "CANCELADO": "CANCELADO",
        "TIMBRADO": "TIMBRADO",
    }

    # Nombre de la tabla
    __tablename__ = "timbrados"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    nomina_id = Column(Integer, ForeignKey("nominas.id"), index=True, nullable=False)
    nomina = relationship("Nomina", back_populates="timbrados")

    # Columnas
    estado = Column(Enum(*ESTADOS, name="timbrados_estados"), nullable=False, index=True)
    archivo_pdf = Column(String(256), nullable=False, default="", server_default="")
    url_pdf = Column(String(512), nullable=False, default="", server_default="")
    archivo_xml = Column(String(256), nullable=False, default="", server_default="")
    url_xml = Column(String(512), nullable=False, default="", server_default="")

    def __repr__(self):
        """Representación"""
        return f"<Timbrado {self.id}>"
