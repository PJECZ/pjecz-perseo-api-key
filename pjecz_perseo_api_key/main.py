"""
PJECZ Perseo API Key
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from .routers.autoridades import autoridades
from .routers.bitacoras import bitacoras
from .routers.distritos import distritos
from .routers.entradas_salidas import entradas_salidas
from .routers.modulos import modulos
from .routers.nominas import nominas
from .routers.permisos import permisos
from .routers.personas import personas
from .routers.puestos import puestos
from .routers.roles import roles
from .routers.tabuladores import tabuladores
from .routers.tareas import tareas
from .routers.timbrados import timbrados
from .routers.usuarios import usuarios
from .routers.usuarios_roles import usuarios_roles
from .settings import get_settings

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
app.include_router(nominas)
app.include_router(permisos)
app.include_router(personas)
app.include_router(puestos)
app.include_router(roles)
app.include_router(tabuladores)
app.include_router(tareas)
app.include_router(timbrados)
app.include_router(usuarios)
app.include_router(usuarios_roles)

# Paginación
add_pagination(app)


# Mensaje de Bienvenida
@app.get("/")
async def root():
    """Mensaje de Bienvenida"""
    return {"message": "API con autentificación para realizar operaciones con la base de datos de Perseo."}
