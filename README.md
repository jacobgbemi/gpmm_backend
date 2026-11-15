# GlintPM Backend — Phase 00 / Foundation

Django + Django REST Framework foundation for the GlintPM mobile application.

## Stack

- Python 3.11+
- Django 5.x
- Django REST Framework
- PostgreSQL
- django-environ
- django-cors-headers

API prefix: `/api/v1/`

## Project layout

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
│   └── common/          # shared utilities, health endpoint
├── tests/
├── requirements/
├── manage.py
├── .env.example
└── README.md
```

## Local setup

### 1. Python virtual environment

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements/development.txt
```

### 2. Environment

```bash
cp .env.example .env
# Edit .env — set DJANGO_SECRET_KEY and DATABASE_URL
```

Generate a secret key if needed:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 3. Database

**PostgreSQL (recommended):**

```bash
# Create database and user (example)
createdb glintpm
# or use your preferred PostgreSQL client
```

**Quick start without PostgreSQL:**

```bash
export USE_SQLITE=true
```

### 4. Migrations and run

```bash
export DJANGO_SETTINGS_MODULE=config.settings.development
python manage.py migrate
python manage.py createsuperuser   # optional
python manage.py runserver
```

- Admin: http://127.0.0.1:8000/admin/
- API root: http://127.0.0.1:8000/api/v1/
- Health: http://127.0.0.1:8000/api/v1/health/

## Tests

```bash
python manage.py test tests
# or
pytest
```

Tests use an in-memory SQLite database and do not require production secrets.

## Health response

```json
{
  "status": "ok",
  "service": "glintpm-backend",
  "version": "v1"
}
```

## Phase scope

This phase delivers only:

- Project structure and split settings
- Environment-based configuration
- PostgreSQL (or SQLite for local convenience)
- DRF and `/api/v1/` routing
- `common` app with health and API root
- Django Admin
- Initial tests and setup documentation

No domain models, authentication, or product APIs are included. Those belong to later phases.

## Branch

Suggested branch name: `backend-phase-00` (or `backend-phase-01` to match the repo’s phase-01 foundation document).

Do not push or merge until the phase is reviewed and approved.
