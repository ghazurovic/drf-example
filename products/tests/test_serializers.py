from django.test import TestCase
from products.models import Product
from products.serializers import ProductSerializer


class ProductTest(TestCase):
    """ Test module for Product model """

    def setUp(self):
        Product.objects.create(name='Headphones', price=200.30, rating=3)

    def test_product_serializer(self):
        product = Product.objects.get(name='Headphones')
        serializer = ProductSerializer(product)
        self.assertEqual(
            serializer.data['name'], 'Headphones')
        self.assertEqual(
            float(serializer.data['rating']), 3)
