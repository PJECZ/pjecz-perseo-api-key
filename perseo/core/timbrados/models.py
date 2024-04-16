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

    @property
    def nomina_fecha_pago(self):
        """Fecha de pago de la nómina"""
        return self.nomina.fecha_pago

    @property
    def nomina_tipo(self):
        """Tipo de la nómina"""
        return self.nomina.tipo

    @property
    def persona_curp(self):
        """CURP de la persona"""
        return self.nomina.persona.curp

    @property
    def persona_rfc(self):
        """RFC de la persona"""
        return self.nomina.persona.rfc

    def __repr__(self):
        """Representación"""
        return f"<Timbrado {self.id}>"
