"""
Development settings for GlintPM backend.
"""
from .base import *  # noqa: F401, F403

DEBUG = True

# Allow all hosts in development for convenience
ALLOWED_HOSTS = ["*"]

# Simpler static file serving in development
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# More verbose logging
LOGGING["root"]["level"] = "DEBUG"  # noqa: F405
LOGGING["loggers"]["django"]["level"] = "INFO"  # noqa: F405
LOGGING["loggers"]["apps"]["level"] = "DEBUG"  # noqa: F405

# DRF: allow browsable API in development
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [  # noqa: F405
    "rest_framework.renderers.JSONRenderer",
    "rest_framework.renderers.BrowsableAPIRenderer",
]

# Optional: Django Debug Toolbar (install separately if desired)
# INSTALLED_APPS += ["debug_toolbar"]
# MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
# INTERNAL_IPS = ["127.0.0.1"]