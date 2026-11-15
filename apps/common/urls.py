"""
Common URL patterns under /api/v1/.
"""
from django.urls import path

from .views import HealthCheckView, health_check_simple

urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health-check"),
    path("health/simple/", health_check_simple, name="health-check-simple"),
]