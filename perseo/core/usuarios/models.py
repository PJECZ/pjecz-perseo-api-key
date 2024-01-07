"""
Usuarios, modelos
"""
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Usuario(Base, UniversalMixin):
    """Usuario"""

    # Nombre de la tabla
    __tablename__ = "usuarios"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Claves foráneas
    autoridad_id = Column(Integer, ForeignKey("autoridades.id"), index=True, nullable=False)
    autoridad = relationship("Autoridad", back_populates="usuarios")

    # Columnas
    email = Column(String(256), nullable=False, unique=True, index=True)
    nombres = Column(String(256), nullable=False)
    apellido_primero = Column(String(256), nullable=False)
    apellido_segundo = Column(String(256))
    curp = Column(String(18), default="", server_default="")
    puesto = Column(String(256), default="", server_default="")

    # Columnas que no deben ser expuestas
    api_key = Column(String(128), nullable=False)
    api_key_expiracion = Column(DateTime(), nullable=False)
    contrasena = Column(String(256), nullable=False)

    # Hijos
    bitacoras = relationship("Bitacora", back_populates="usuario", lazy="noload")
    entradas_salidas = relationship("EntradaSalida", back_populates="usuario", lazy="noload")
    tareas = relationship("Tarea", back_populates="usuario")
    usuarios_roles = relationship("UsuarioRol", back_populates="usuario")

    @property
    def distrito_id(self):
        """Distrito ID"""
        return self.autoridad.distrito_id

    @property
    def distrito_clave(self):
        """Distrito clave"""
        return self.autoridad.distrito.clave

    @property
    def distrito_nombre(self):
        """Distrito nombre"""
        return self.autoridad.distrito.nombre

    @property
    def distrito_nombre_corto(self):
        """Distrito nombre corto"""
        return self.autoridad.distrito.nombre_corto

    @property
    def autoridad_clave(self):
        """Autoridad clave"""
        return self.autoridad.clave

    @property
    def autoridad_descripcion(self):
        """Autoridad descripción"""
        return self.autoridad.descripcion

    @property
    def autoridad_descripcion_corta(self):
        """Autoridad descripción corta"""
        return self.autoridad.descripcion_corta

    @property
    def nombre(self):
        """Junta nombres, apellido_primero y apellido_segundo"""
        return self.nombres + " " + self.apellido_primero + " " + self.apellido_segundo

    @classmethod
    def find_by_identity(cls, identity):
        """Encontrar a un usuario por su correo electrónico"""
        return Usuario.query.filter(Usuario.email == identity).first()

    @property
    def is_active(self):
        """¿Es activo?"""
        return self.estatus == "A"

    @property
    def permissions(self):
        """Permisos"""
        return self.rol.permissions

    def can(self, perm):
        """¿Tiene permiso?"""
        return self.rol.has_permission(perm)

    def can_view(self, module):
        """¿Tiene permiso para ver?"""
        return self.rol.can_view(module)

    def __repr__(self):
        """Representación"""
        return f"<Usuario {self.email}>"
