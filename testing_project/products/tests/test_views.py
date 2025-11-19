from django.test import TestCase, SimpleTestCase

class TestHomePage(SimpleTestCase):

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)