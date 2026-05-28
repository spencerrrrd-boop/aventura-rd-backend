from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.reserva import Reserva
from app.models.oferta import Oferta
from app.schemas.reserva import ReservaCreate, ReservaResponse
from typing import List
from decimal import Decimal

router = APIRouter(
    prefix="/reservas",
    tags=["Reservas"]
)

@router.post("/", response_model=ReservaResponse, status_code=201)
def create_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    # Verificar que la oferta existe y está activa
    oferta = db.query(Oferta).filter(
        Oferta.id == reserva.oferta_id,
        Oferta.activa == True
    ).first()

    if not oferta:
        raise HTTPException(status_code=404, detail="Oferta no encontrada o no disponible")

    # Verificar cupos disponibles
    if oferta.cupos_disponibles < reserva.num_personas:
        raise HTTPException(status_code=400, detail="No hay suficientes cupos disponibles")

    # Calcular total
    total = Decimal(str(oferta.precio)) * reserva.num_personas

    # Crear reserva
    nueva_reserva = Reserva(
        **reserva.model_dump(),
        total_pago=total
    )

    # Reducir cupos
    oferta.cupos_disponibles -= reserva.num_personas

    db.add(nueva_reserva)
    db.commit()
    db.refresh(nueva_reserva)

    return nueva_reserva

@router.get("/", response_model=List[ReservaResponse])
def get_reservas(db: Session = Depends(get_db)):
    reservas = db.query(Reserva).all()
    return reservas

@router.get("/{reserva_id}", response_model=ReservaResponse)
def get_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()

    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")

    return reserva