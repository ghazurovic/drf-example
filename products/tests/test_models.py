from django.test import TestCase
from products.models import Product


class ProductTest(TestCase):
    """ Test module for Product model """

    def setUp(self):
        Product.objects.bulk_create([
            Product(name='Headphones', price=200.30, rating=3),
            Product(name='Keyboard', price=179, rating=4),
            Product(name='Notebook', price=3799, rating=5),
            Product(name='Display', price=450, rating=1),
            Product(name='Table', price=1850, rating=2)
        ])

    def test_product(self):
        product_1 = Product.objects.get(name='Headphones')
        product_2 = Product.objects.get(name='Display')
        self.assertEqual(
            product_1.name, 'Headphones')
        self.assertEqual(
            product_2.name, 'Display')
