from app.database import SessionLocal
from app.models.categoria import Categoria
from app.models.oferta import Oferta
from app.models.administrador import Administrador
from cryptography.fernet import Fernet
import bcrypt

def seed_categorias(db):
    categorias = [
        Categoria(nombre="Senderismo", descripcion="Rutas y trekking por la naturaleza dominicana"),
        Categoria(nombre="Rafting", descripcion="Descenso de ríos y rápidos emocionantes"),
        Categoria(nombre="Zipline", descripcion="Canopy y tirolesas sobre el bosque"),
        Categoria(nombre="Escalada", descripcion="Escalada en roca y montaña"),
        Categoria(nombre="Camping", descripcion="Noches bajo las estrellas en la naturaleza"),
        Categoria(nombre="Ciclismo", descripcion="Mountain bike por senderos y montañas"),
    ]
    db.add_all(categorias)
    db.commit()
    print("✅ Categorías creadas")
    return categorias

def seed_ofertas(db, categorias):
    ofertas = [
        Oferta(
            titulo="Trekking Pico Duarte",
            descripcion="La aventura más desafiante de República Dominicana. Sube al pico más alto del Caribe a través de senderos únicos rodeados de pinos y naturaleza virgen.",
            imagen_url="https://images.unsplash.com/photo-1551632811-561732d1e306?w=800",
            precio=4500.00,
            duracion_dias=3,
            destino="La Ciénaga, La Vega",
            itinerario="Día 1: Llegada y campamento base. Día 2: Ascenso al pico (3,098 msnm). Día 3: Descenso y regreso.",
            cupos_disponibles=12,
            categoria_id=categorias[0].id
        ),
        Oferta(
            titulo="Rafting Río Yaque del Norte",
            descripcion="Adrenalina pura en el río más largo del Caribe. Navega rápidos emocionantes rodeado de la exuberante naturaleza de Jarabacoa.",
            imagen_url="https://images.unsplash.com/photo-1530866495561-507c9faab2ed?w=800",
            precio=2800.00,
            duracion_dias=1,
            destino="Jarabacoa, La Vega",
            itinerario="08:00 Llegada. 09:00 Briefing de seguridad. 10:00 Descenso del río (3 horas). 13:00 Almuerzo incluido. 15:00 Regreso.",
            cupos_disponibles=15,
            categoria_id=categorias[1].id
        ),
        Oferta(
            titulo="Zipline Jarabacoa",
            descripcion="Vuela sobre el bosque tropical dominicano a más de 80 km/h. Una experiencia de tirolesa incomparable con vistas espectaculares al valle de Jarabacoa.",
            imagen_url="https://images.unsplash.com/photo-1521673461164-de300ebcfb17?w=800",
            precio=1500.00,
            duracion_dias=1,
            destino="Jarabacoa, La Vega",
            itinerario="09:00 Llegada. 09:30 Equipo y seguridad. 10:00 Circuito de 8 cables (2 horas). 12:00 Fin de la actividad.",
            cupos_disponibles=20,
            categoria_id=categorias[2].id
        ),
        Oferta(
            titulo="Escalada Salto de Jimenoa",
            descripcion="Combina escalada en roca con una de las cascadas más bellas de República Dominicana. Perfecto para aventureros con experiencia básica.",
            imagen_url="https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=800",
            precio=3200.00,
            duracion_dias=2,
            destino="Jarabacoa, La Vega",
            itinerario="Día 1: Llegada, escalada en roca y campamento. Día 2: Visita al Salto de Jimenoa y regreso.",
            cupos_disponibles=8,
            categoria_id=categorias[3].id
        ),
        Oferta(
            titulo="Camping Valle Nuevo",
            descripcion="Duerme bajo un cielo lleno de estrellas en el Parque Nacional Valle Nuevo a 2,200 metros de altura. Una experiencia única de desconexión total.",
            imagen_url="https://images.unsplash.com/photo-1478131143081-80f7f84ca84d?w=800",
            precio=2000.00,
            duracion_dias=2,
            destino="Constanza, La Vega",
            itinerario="Día 1: Llegada, senderismo y fogata. Día 2: Amanecer en el valle, desayuno y regreso.",
            cupos_disponibles=10,
            categoria_id=categorias[4].id
        ),
        Oferta(
            titulo="MTB Constanza",
            descripcion="Recorre los senderos de montaña de Constanza en bicicleta todo terreno. Paisajes únicos de pinos, fresas y vegetación de altura que no encontrarás en otro lugar del Caribe.",
            imagen_url="https://images.unsplash.com/photo-1544191696-102dbdaeeaa0?w=800",
            precio=1800.00,
            duracion_dias=1,
            destino="Constanza, La Vega",
            itinerario="08:00 Llegada. 08:30 Selección de bicicleta y ruta. 09:00 Recorrido de 25km (4 horas). 13:00 Almuerzo y regreso.",
            cupos_disponibles=12,
            categoria_id=categorias[5].id
        ),
    ]
    db.add_all(ofertas)
    db.commit()
    print("✅ Ofertas creadas")

def seed_admin(db):
    password = "admin123"
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")
    
    admin = Administrador(
        nombre="Administrador AventuraRD",
        email="admin@aventurard.com",
        password_hash=password_hash,
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
        print("🌱 Iniciando seed de datos...")
        categorias = seed_categorias(db)
        seed_ofertas(db, categorias)
        seed_admin(db)
        print("🎉 Seed completado exitosamente")
    except Exception as e:
        print(f"❌ Error en seed: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    run_seed()