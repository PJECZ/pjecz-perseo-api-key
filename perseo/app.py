"""
PJECZ Perseo API Key
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from config.settings import get_settings

from .v4.autoridades.paths import autoridades
from .v4.bitacoras.paths import bitacoras
from .v4.distritos.paths import distritos
from .v4.entradas_salidas.paths import entradas_salidas
from .v4.modulos.paths import modulos
from .v4.permisos.paths import permisos
from .v4.roles.paths import roles
from .v4.tareas.paths import tareas
from .v4.usuarios.paths import usuarios
from .v4.usuarios_roles.paths import usuarios_roles


def create_app() -> FastAPI:
    """Crea la aplicación FastAPI"""

    # FastAPI
    app = FastAPI(
        title="PJECZ Perseo API Key",
        description="API con autentificación para realizar operaciones con la base de datos de Perseo.",
        docs_url="/docs",
        redoc_url=None,
    )

    # CORSMiddleware
    settings = get_settings()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.origins.split(","),
        allow_credentials=False,
        allow_methods=["GET"],
        allow_headers=["*"],
    )

    # Rutas
    app.include_router(autoridades)
    app.include_router(bitacoras)
    app.include_router(distritos)
    app.include_router(entradas_salidas)
    app.include_router(modulos)
    app.include_router(permisos)
    app.include_router(roles)
    app.include_router(tareas)
    app.include_router(usuarios)
    app.include_router(usuarios_roles)

    # Paginación
    add_pagination(app)

    # Mensaje de Bienvenida
    @app.get("/")
    async def root():
        """Mensaje de Bienvenida"""
        return {"message": "API con autentificación para realizar operaciones con la base de datos de Perseo."}

    # Entregar
    return app
