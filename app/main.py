from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app import models
from app.routers import categorias, ofertas, reservas, auth, admin

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AventuraRD API",
    description="API REST para la plataforma de ecoturismo y aventura AventuraRD",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://astonishing-banoffee-43cee5.netlify.app",
        "http://localhost:3000",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas públicas
app.include_router(categorias.router)
app.include_router(ofertas.router)
app.include_router(reservas.router)

# Rutas de autenticación
app.include_router(auth.router)

# Rutas de administración (protegidas con JWT)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a AventuraRD API 🏔️"}

@app.get("/health")
def health():
    return {"status": "ok", "app": "AventuraRD API"}