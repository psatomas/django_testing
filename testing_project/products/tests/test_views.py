from django.test import TestCase, SimpleTestCase
from products.models import Product
from django.urls import reverse

class TestHomePage(SimpleTestCase):

    def test_homepage_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_homepage_contains_Welcome_message(self):
        response = self.client.get('/')
        self.assertContains(response, 'Welcome to Our Store!', status_code=200)

class TestProductsPage(TestCase):

    def setUp(self):
        Product.objects.create(name="Laptop", price=1000)
        Product.objects.create(name="Laptop", price=800)



