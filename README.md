# GlintPM Backend — Phase 01 Foundation

Django + Django REST Framework foundation for the GlintPM mobile application.

## Requirements

- Python 3.11+ (3.12 recommended)
- PostgreSQL 14+ (SQLite is used automatically if `DATABASE_URL` is not set)
- Virtual environment recommended

## Quick start

```bash
# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements/development.txt

# 3. Configure environment
cp .env.example .env
# Edit .env and set at least DJANGO_SECRET_KEY

# 4. Run migrations
python manage.py migrate

# 5. Create a superuser (optional, for admin)
python manage.py createsuperuser

# 6. Start development server
python manage.py runserver
```

## Endpoints (Phase 01)

| Method | Path                    | Description                          |
|--------|-------------------------|--------------------------------------|
| GET    | `/api/v1/health/`       | Health check (includes DB status)    |
| GET    | `/api/v1/health/simple/`| Lightweight health check             |
| GET    | `/admin/`               | Django Admin (Unfold theme)          |

Example health response:

```json
{
  "status": "ok",
  "service": "glintpm-backend",
  "version": "v1",
  "database": "connected"
}
```

## Project structure

```text
backend/
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── apps/
│   └── common/          # shared utilities, health checks
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── tests/
├── manage.py
├── .env.example
└── README.md
```

## Settings modules

- Development (default): `config.settings.development`
- Production: `config.settings.production`

Set via environment variable:

```bash
export DJANGO_SETTINGS_MODULE=config.settings.production
```

## Tests

```bash
python manage.py test
# or
pytest
```

## Notes

- Secrets must never be committed. Use `.env` (gitignored) and `.env.example`.
- PostgreSQL is the target database. SQLite is accepted only for local bootstrap when `DATABASE_URL` is unset.
- No domain models or business APIs are implemented in Phase 01.
