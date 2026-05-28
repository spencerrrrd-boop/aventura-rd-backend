from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.administrador import Administrador
from app.schemas.administrador import LoginRequest, TokenResponse, AdminResponse
from app.core.security import verify_password, create_access_token
from datetime import timedelta
from app.config import settings

router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"]
)

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    # Buscar administrador por email
    admin = db.query(Administrador).filter(
        Administrador.email == request.email,
        Administrador.activo == True
    ).first()

    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos"
        )

    # Verificar contraseña
    if not verify_password(request.password, admin.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos"
        )

    # Generar token JWT
    access_token = create_access_token(
        data={"sub": str(admin.id)},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        admin=AdminResponse.model_validate(admin)
    )

@router.get("/me", response_model=AdminResponse)
def get_me(db: Session = Depends(get_db)):
    return {"mensaje": "Endpoint protegido próximamente"}