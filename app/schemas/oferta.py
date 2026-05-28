from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from app.schemas.categoria import CategoriaResponse

class OfertaBase(BaseModel):
    titulo: str
    descripcion: str
    imagen_url: str | None = None
    precio: Decimal
    duracion_dias: int
    destino: str
    itinerario: str | None = None
    cupos_disponibles: int
    categoria_id: int

class OfertaCreate(OfertaBase):
    pass

class OfertaUpdate(BaseModel):
    titulo: str | None = None
    descripcion: str | None = None
    imagen_url: str | None = None
    precio: Decimal | None = None
    duracion_dias: int | None = None
    destino: str | None = None
    itinerario: str | None = None
    cupos_disponibles: int | None = None
    activa: bool | None = None
    categoria_id: int | None = None

class OfertaResponse(OfertaBase):
    id: int
    activa: bool
    created_at: datetime
    updated_at: datetime
    categoria: CategoriaResponse

    class Config:
        from_attributes = True