from django.core.exceptions import ValidationError
from django.test import TestCase
from products.models import Product
from django.db import IntegrityError

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product(name="Test Product", price=100.00, stock_count=10)

    def test_in_stock_property(self):
        self.assertTrue(self.product.in_stock)

        self.product.stock_count = 0
        self.assertFalse(self.product.in_stock)

    def test_get_discounted_price(self):
        self.assertEqual(self.product.get_discounted_price(10), 90)
        self.assertEqual(self.product.get_discounted_price(50), 50)
        self.assertEqual(self.product.get_discounted_price(0), 100)

    def test_negative_price_validation(self):
        self.product.price = -10
        with self.assertRaises(ValidationError):
            self.product.clean()

    def test_negative_stock_count_validation(self):
        self.product.stock_count = -10
        with self.assertRaises(ValidationError):
            self.product.clean()

    def test_negative_price_constraint(self):
        """Test that a product with a negative price cannot be saved due to database constraints."""
        product = Product(name="Negative Price Product", price=-1.00, stock_count=5)

        with self.assertRaises(IntegrityError):
            product.save()

    def test_negative_stock_count_constraint(self):
        """Test that a product with a negative stock count cannot be saved due to database constraints."""
        product = Product(name="Negative Price Product", price=1.00, stock_count=-5)

        with self.assertRaises(IntegrityError):
            product.save()