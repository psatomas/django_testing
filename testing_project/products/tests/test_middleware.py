from django.test import TestCase
from django.urls import reverse


class MaintenanceModeTests(TestCase):
    def test_maintenance_mode_off(self):
        """Test that the site is accessible when maintenance mode is off."""
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Welcome to Our Store!', status_code=200)