"""
Nominas, modelos
"""
from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Nomina(Base, UniversalMixin):
    """Nomina"""

    TIPOS = {
        "AGUINALDO": "AGUINALDO",
        "APOYO ANUAL": "APOYO ANUAL",
        "DESPENSA": "DESPENSA",
        "SALARIO": "SALARIO",
    }

    # Nombre de la tabla
    __tablename__ = "nominas"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    persona_id = Column(Integer, ForeignKey("personas.id"), index=True, nullable=False)
    persona = relationship("Persona", back_populates="nominas")

    # Columnas
    fecha_pago = Column(Date(), nullable=False)
    tipo = Column(Enum(*TIPOS, name="nominas_tipos"), nullable=False, index=True)
    timbrado_id = Column(Integer())  # Pueder ser nulo o el ID del Timbrado

    # Hijos
    timbrados = relationship("Timbrado", back_populates="nomina")

    @property
    def persona_curp(self):
        """CURP de la persona"""
        return self.persona.curp

    @property
    def persona_rfc(self):
        """RFC de la persona"""
        return self.persona.rfc

    def __repr__(self):
        """Representación"""
        return f"<Nomina {self.id}>"
