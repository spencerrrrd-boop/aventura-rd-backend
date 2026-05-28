from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app import models

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AventuraRD API",
    description="API REST para la plataforma de ecoturismo y aventura AventuraRD",
    version="1.0.0"
)

# Configurar CORS para que el Frontend pueda consumir la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a AventuraRD API 🏔️"}

@app.get("/health")
def health():
    return {"status": "ok", "app": "AventuraRD API"}