"""
Development settings for GlintPM backend.
"""
from .base import *  # noqa: F401, F403

DEBUG = True

# More permissive hosts for local development
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0", "[::1]"]

# Allow all origins in development (tighten for production)
CORS_ALLOW_ALL_ORIGINS = True

# Optional: use SQLite when PostgreSQL is not available (set USE_SQLITE=true)
import os

if os.environ.get("USE_SQLITE", "false").lower() in ("1", "true", "yes"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Development-friendly logging
LOGGING["root"]["level"] = "DEBUG"  # noqa: F405
LOGGING["loggers"]["django"]["level"] = "INFO"  # noqa: F405

# Email backend for development (console)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
