from django.test import TestCase
from django.urls import reverse
from products.models import Product

class ProductFormTest(TestCase):
    
    def test_create_product_when_submitting_valid_form(self):
        """Test that form submission with valid data creates a product in the database."""
        form_data = {
            'name': 'Tablet',
            'price': 299.99,
            'stock_count': 50,
        }
        response = self.client.post(reverse('products'), data=form_data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.objects.filter(name='Tablet').exists())

    def test_dont_create_product_when_submitting_invalid_form(self):
        """Test form submission with invalid data does not create a product."""
        form_data = {
            'name': '',
            'price': -50.00,
            'stock_count': -5,
        }
        response = self.client.post(reverse('products'), data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue("form" in response.context)

        form = response.context['form']
        self.assertFormError(form, 'name', 'This field is required.')
        self.assertFormError(form, 'price', 'Price cannot be negative')
        self.assertFormError(form, 'stock_count', 'Stock count cannot be negative')

        self.assertFalse(Product.objects.exists())