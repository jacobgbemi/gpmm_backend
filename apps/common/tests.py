"""
Tests for the common app and foundation.
"""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class HealthCheckTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_health_endpoint_returns_ok(self):
        """Health endpoint returns 200 and expected payload shape."""
        url = reverse("health-check")
        response = self.client.get(url)
        self.assertIn(response.status_code, (status.HTTP_200_OK, status.HTTP_503_SERVICE_UNAVAILABLE))
        data = response.json()
        self.assertIn("status", data)
        self.assertIn("service", data)
        self.assertEqual(data["service"], "glintpm-backend")
        self.assertIn("version", data)
        self.assertEqual(data["version"], "v1")
        self.assertIn("database", data)

    def test_simple_health_endpoint(self):
        """Simple health endpoint always returns 200."""
        url = reverse("health-check-simple")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["service"], "glintpm-backend")

    def test_api_v1_root_resolves(self):
        """API v1 prefix is wired (health lives under it)."""
        response = self.client.get("/api/v1/health/")
        self.assertIn(response.status_code, (status.HTTP_200_OK, status.HTTP_503_SERVICE_UNAVAILABLE))


class AdminTests(TestCase):
    def test_admin_login_page_loads(self):
        """Admin login page is reachable."""
        response = self.client.get("/admin/login/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProjectSmokeTests(TestCase):
    def test_project_starts_with_development_settings(self):
        """Basic smoke: Django settings are loadable."""
        from django.conf import settings

        self.assertTrue(hasattr(settings, "INSTALLED_APPS"))
        self.assertIn("apps.common", settings.INSTALLED_APPS)
        self.assertIn("rest_framework", settings.INSTALLED_APPS)
