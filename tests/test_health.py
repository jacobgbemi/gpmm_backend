"""
Tests for health and API root endpoints (Phase 00 foundation).
"""
from django.test import TestCase, override_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


@override_settings(
    # Use in-memory SQLite so tests run without PostgreSQL
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    }
)
class HealthCheckTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_health_endpoint_returns_ok(self):
        url = reverse("health")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "ok")
        self.assertEqual(response.data["service"], "glintpm-backend")
        self.assertEqual(response.data["version"], "v1")

    def test_health_endpoint_is_public(self):
        """Health must not require authentication."""
        url = reverse("health")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_root_resolves(self):
        url = reverse("api-root")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("message", response.data)
        self.assertIn("endpoints", response.data)
        self.assertIn("health", response.data["endpoints"])
