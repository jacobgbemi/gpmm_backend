"""
Common API views — health and API root for Phase 00 foundation.
"""
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    """
    Minimal health endpoint.
    Confirms the application is running without exposing secrets or internal config.
    """

    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        return Response(
            {
                "status": "ok",
                "service": "glintpm-backend",
                "version": "v1",
            }
        )


class APIRootView(APIView):
    """
    API version root under /api/v1/.
    Lists available top-level resources as they are added in later phases.
    """

    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        return Response(
            {
                "message": "GlintPM API v1",
                "endpoints": {
                    "health": request.build_absolute_uri("health/"),
                },
            }
        )
