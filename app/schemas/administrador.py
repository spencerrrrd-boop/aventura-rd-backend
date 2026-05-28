from pydantic import BaseModel, EmailStr
from datetime import datetime

class AdminCreate(BaseModel):
    nombre: str
    email: EmailStr
    password: str

class AdminResponse(BaseModel):
    id: int
    nombre: str
    email: str
    activo: bool
    created_at: datetime

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    admin: AdminResponse