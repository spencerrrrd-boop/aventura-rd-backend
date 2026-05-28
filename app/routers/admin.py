from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.administrador import Administrador
from app.models.oferta import Oferta
from app.models.reserva import Reserva
from app.schemas.oferta import OfertaCreate, OfertaUpdate, OfertaResponse
from app.schemas.reserva import ReservaResponse, ReservaEstadoUpdate
from app.schemas.administrador import AdminCreate, AdminResponse
from app.core.security import get_password_hash
from app.core.dependencies import get_current_admin
from typing import List
from sqlalchemy.orm import joinedload

router = APIRouter(
    prefix="/admin",
    tags=["Administración"]
)

# ─── DASHBOARD ───────────────────────────────────────────
@router.get("/dashboard")
def get_dashboard(
    db: Session = Depends(get_db),
    current_admin: Administrador = Depends(get_current_admin)
):
    total_ofertas = db.query(Oferta).filter(Oferta.activa == True).count()
    total_reservas = db.query(Reserva).count()
    reservas_pendientes = db.query(Reserva).filter(Reserva.estado == "pendiente").count()
    reservas_confirmadas = db.query(Reserva).filter(Reserva.estado == "confirmada").count()
    
    ingresos = db.query(Reserva).filter(
        Reserva.estado != "cancelada"
    ).all()
    total_ingresos = sum(float(r.total_pago) for r in ingresos)

    return {
        "total_ofertas_activas": total_ofertas,
        "total_reservas": total_reservas,
        "reservas_pendientes": reservas_pendientes,
        "reservas_confirmadas": reservas_confirmadas,
        "total_ingresos": total_ingresos
    }

# ─── GESTIÓN DE OFERTAS ──────────────────────────────────
@router.post("/ofertas", response_model=OfertaResponse, status_code=201)
def create_oferta(
    oferta: OfertaCreate,
    db: Session = Depends(get_db),
    current_admin: Administrador = Depends(get_current_admin)
):
    nueva_oferta = Oferta(**oferta.model_dump())
    db.add(nueva_oferta)
    db.commit()
    db.refresh(nueva_oferta)
    oferta_con_categoria = db.query(Oferta).options(
        joinedload(Oferta.categoria)
    ).filter(Oferta.id == nueva_oferta.id).first()
    return oferta_con_categoria

@router.put("/ofertas/{oferta_id}", response_model=OfertaResponse)
def update_oferta(
    oferta_id: int,
    oferta_update: OfertaUpdate,
    db: Session = Depends(get_db),
    current_admin: Administrador = Depends(get_current_admin)
):
    oferta = db.query(Oferta).filter(Oferta.id == oferta_id).first()
    if not oferta:
        raise HTTPException(status_code=404, detail="Oferta no encontrada")

    for key, value in oferta_update.model_dump(exclude_unset=True).items():
        setattr(oferta, key, value)

    db.commit()
    db.refresh(oferta)
    oferta_con_categoria = db.query(Oferta).options(
        joinedload(Oferta.categoria)
    ).filter(Oferta.id == oferta.id).first()
    return oferta_con_categoria

@router.delete("/ofertas/{oferta_id}")
def delete_oferta(
    oferta_id: int,
    db: Session = Depends(get_db),
    current_admin: Administrador = Depends(get_current_admin)
):
    oferta = db.query(Oferta).filter(Oferta.id == oferta_id).first()
    if not oferta:
        raise HTTPException(status_code=404, detail="Oferta no encontrada")

    oferta.activa = False
    db.commit()
    return {"mensaje": f"Oferta {oferta_id} desactivada correctamente"}

# ─── GESTIÓN DE RESERVAS ─────────────────────────────────
@router.get("/reservas", response_model=List[ReservaResponse])
def get_reservas_admin(
    db: Session = Depends(get_db),
    current_admin: Administrador = Depends(get_current_admin)
):
    return db.query(Reserva).all()

@router.patch("/reservas/{reserva_id}/estado", response_model=ReservaResponse)
def update_estado_reserva(
    reserva_id: int,
    estado_update: ReservaEstadoUpdate,
    db: Session = Depends(get_db),
    current_admin: Administrador = Depends(get_current_admin)
):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")

    reserva.estado = estado_update.estado
    db.commit()
    db.refresh(reserva)
    return reserva

# ─── GESTIÓN DE ADMINISTRADORES ──────────────────────────
@router.post("/usuarios", response_model=AdminResponse, status_code=201)
def create_admin(
    admin_data: AdminCreate,
    db: Session = Depends(get_db),
    current_admin: Administrador = Depends(get_current_admin)
):
    existing = db.query(Administrador).filter(
        Administrador.email == admin_data.email
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    nuevo_admin = Administrador(
        nombre=admin_data.nombre,
        email=admin_data.email,
        password_hash=get_password_hash(admin_data.password),
        activo=True
    )
    db.add(nuevo_admin)
    db.commit()
    db.refresh(nuevo_admin)
    return nuevo_admin

@router.get("/usuarios", response_model=List[AdminResponse])
def get_admins(
    db: Session = Depends(get_db),
    current_admin: Administrador = Depends(get_current_admin)
):
    return db.query(Administrador).filter(Administrador.activo == True).all()