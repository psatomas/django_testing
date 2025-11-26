from django.test import TestCase, override_settings
from django.urls import reverse


class MaintenanceModeTests(TestCase):

    @override_settings(MAINTENANCE_MODE=False)
    def test_maintenance_mode_off(self):
        """Test that the site is accessible when maintenance mode is off."""
        response = self.client.get(reverse('home'))

        self.assertContains(response, "Welcome to Our Store!", status_code=200)

    @override_settings(MAINTENANCE_MODE=True)
    def test_maintenance_mode_on(self):
        """Test that the site is accessible when maintenance mode is off."""
        response = self.client.get(reverse('home'))

        self.assertContains(response, "Site is under maintenance", status_code=503)