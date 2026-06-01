# AventuraRD — Backend API

API REST para la plataforma de ecoturismo y aventura AventuraRD, construida con FastAPI y conectada a MySQL en Aiven.

## 🚀 Demo en producción

**API URL:** https://aventura-rd-api.onrender.com

## 🛠️ Tecnologías

- Python 3.10
- FastAPI
- SQLAlchemy
- MySQL (Aiven Cloud)
- JWT (autenticación)
- Poetry (gestión de dependencias)
- Render (despliegue)

## 📁 Estructura de carpetas
aventura-rd-backend/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   └── core/
├── database/
├── requirements.txt
├── Procfile
└── README.md

## ⚙️ Instalación local

1. Clona el repositorio
```bash
git clone https://github.com/TU_USUARIO/aventura-rd-backend.git
cd aventura-rd-backend
```

2. Instala Poetry y las dependencias
```bash
poetry install
```

3. Crea el archivo `.env` basado en `.env.example`
```bash
cp .env.example .env
```

4. Configura las variables de entorno en `.env`
DB_HOST=tu-host
DB_PORT=3306
DB_NAME=defaultdb
DB_USER=tu-usuario
DB_PASSWORD=tu-password
SECRET_KEY=tu-clave-secreta

5. Ejecuta el servidor
```bash
poetry run uvicorn app.main:app --reload
```

## 📌 Endpoints principales

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /ofertas | Lista todas las ofertas |
| GET | /ofertas/{id} | Detalle de una oferta |
| POST | /reservas | Crear una reserva |
| GET | /reservas | Lista de reservas |
| GET | /categorias | Lista de categorías |
| POST | /auth/login | Login de administrador |
| GET | /admin/dashboard | Estadísticas (admin) |

## 🗄️ Base de datos

4 tablas: `categorias`, `ofertas`, `reservas`, `administradores`

## 👥 Créditos

Desarrollado por spencer perez, elison roa — Proyecto Final Desarrollo Web
