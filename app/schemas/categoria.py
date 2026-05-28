from pydantic import BaseModel
from datetime import datetime

class CategoriaBase(BaseModel):
    nombre: str
    descripcion: str | None = None

class CategoriaResponse(CategoriaBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True