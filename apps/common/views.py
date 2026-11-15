"""
Common views — health check and shared API infrastructure.
"""
from django.db import connection
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    """
    Minimal health endpoint.
    Confirms application availability without exposing secrets or internal configuration.
    """

    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        db_ok = False
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                db_ok = cursor.fetchone() is not None
        except Exception:
            db_ok = False

        status_code = 200 if db_ok else 503
        payload = {
            "status": "ok" if db_ok else "degraded",
            "service": "glintpm-backend",
            "version": "v1",
            "database": "connected" if db_ok else "unavailable",
        }
        return Response(payload, status=status_code)


def health_check_simple(request):
    """
    Lightweight health check that does not depend on DRF.
    Useful for load balancers and container probes.
    """
    return JsonResponse(
        {
            "status": "ok",
            "service": "glintpm-backend",
        }
    )
