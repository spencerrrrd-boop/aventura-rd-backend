from app.database import SessionLocal
from app.models.categoria import Categoria
from app.models.oferta import Oferta
from app.models.administrador import Administrador

def seed_admin(db):
    from app.core.security import get_password_hash
    
    existing = db.query(Administrador).filter(
        Administrador.email == "admin@aventurard.com"
    ).first()
    
    if existing:
        existing.password_hash = get_password_hash("admin123")
        db.commit()
        print("✅ Administrador actualizado con hash correcto")
    else:
        admin = Administrador(
            nombre="Administrador AventuraRD",
            email="admin@aventurard.com",
            password_hash=get_password_hash("admin123"),
            activo=True
        )
        db.add(admin)
        db.commit()
        print("✅ Administrador creado")
    
    print("   Email: admin@aventurard.com")
    print("   Password: admin123")

def run_seed():
    db = SessionLocal()
    try:
        print("🔧 Actualizando imagen del Zipline...")
        oferta = db.query(Oferta).filter(Oferta.id == 3).first()
        if oferta:
            oferta.imagen_url = "https://images.unsplash.com/photo-1439792675105-701e6a4ab6f0?w=800"
            db.commit()
            print(f"✅ Imagen actualizada: {oferta.imagen_url}")
        else:
            print("❌ Oferta no encontrada")
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()
