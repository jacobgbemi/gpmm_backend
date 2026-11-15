"""
Common models and base classes.
No domain models in Phase 01.
"""
from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract base model that provides created_at and updated_at timestamps.
    Intended for reuse by domain models in later phases.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
