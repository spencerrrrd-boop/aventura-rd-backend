from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from decimal import Decimal
from app.models.reserva import EstadoReserva

class ReservaBase(BaseModel):
    nombre_cliente: str
    apellido_cliente: str
    email: EmailStr
    telefono: str
    oferta_id: int
    fecha_reserva: date
    num_personas: int
    metodo_pago: str
    notas: str | None = None

class ReservaCreate(ReservaBase):
    pass

class ReservaResponse(ReservaBase):
    id: int
    total_pago: Decimal
    estado: EstadoReserva
    created_at: datetime

    class Config:
        from_attributes = True

class ReservaEstadoUpdate(BaseModel):
    estado: EstadoReserva