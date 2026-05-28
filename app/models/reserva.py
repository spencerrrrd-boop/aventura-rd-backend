from sqlalchemy import Column, Integer, String, Text, Numeric, Date, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import enum

class EstadoReserva(str, enum.Enum):
    pendiente = "pendiente"
    confirmada = "confirmada"
    cancelada = "cancelada"
    completada = "completada"

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    nombre_cliente = Column(String(100), nullable=False)
    apellido_cliente = Column(String(100), nullable=False)
    email = Column(String(200), nullable=False)
    telefono = Column(String(20), nullable=False)
    oferta_id = Column(Integer, ForeignKey("ofertas.id"), nullable=False)
    fecha_reserva = Column(Date, nullable=False)
    num_personas = Column(Integer, nullable=False, default=1)
    total_pago = Column(Numeric(10, 2), nullable=False)
    metodo_pago = Column(String(50), nullable=False)
    estado = Column(Enum(EstadoReserva), default=EstadoReserva.pendiente)
    notas = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relación
    oferta = relationship("Oferta", back_populates="reservas")