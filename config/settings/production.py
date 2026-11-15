"""
Production settings for GlintPM backend.
"""
from .base import *  # noqa: F401, F403

DEBUG = False

# Require explicit secret key in production
if SECRET_KEY == "change-me-in-production-insecure-default":  # noqa: F405
    raise ValueError("DJANGO_SECRET_KEY must be set in production")

# Security headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Prefer HTTPS
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=True)  # noqa: F405
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# CORS must be explicit
CORS_ALLOW_ALL_ORIGINS = False
