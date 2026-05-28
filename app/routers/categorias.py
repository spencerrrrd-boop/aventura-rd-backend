from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.categoria import Categoria
from app.schemas.categoria import CategoriaResponse
from typing import List

router = APIRouter(
    prefix="/categorias",
    tags=["Categorías"]
)

@router.get("/", response_model=List[CategoriaResponse])
def get_categorias(db: Session = Depends(get_db)):
    categorias = db.query(Categoria).all()
    return categorias