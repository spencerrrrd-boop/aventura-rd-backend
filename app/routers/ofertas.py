from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload
from app.database import get_db
from app.models.oferta import Oferta
from app.schemas.oferta import OfertaResponse
from typing import List, Optional

router = APIRouter(
    prefix="/ofertas",
    tags=["Ofertas"]
)

@router.get("/", response_model=List[OfertaResponse])
def get_ofertas(
    categoria_id: Optional[int] = Query(None),
    destino: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Oferta).options(
        joinedload(Oferta.categoria)
    ).filter(Oferta.activa == True)

    if categoria_id:
        query = query.filter(Oferta.categoria_id == categoria_id)
    if destino:
        query = query.filter(Oferta.destino.ilike(f"%{destino}%"))

    return query.all()

@router.get("/{oferta_id}", response_model=OfertaResponse)
def get_oferta(oferta_id: int, db: Session = Depends(get_db)):
    oferta = db.query(Oferta).options(
        joinedload(Oferta.categoria)
    ).filter(Oferta.id == oferta_id).first()

    if not oferta:
        raise HTTPException(status_code=404, detail="Oferta no encontrada")

    return oferta