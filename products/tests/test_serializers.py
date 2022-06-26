from django.test import TestCase
from products.models import Product
from products.serializers import ProductSerializer


class ProductTest(TestCase):
    """ Test module for Product model """

    def setUp(self):
        Product.objects.create(name='Headphones', price=200.30, rating=3)

    def test_product_serializer(self):
        instance = Product.objects.get(name='Headphones')
        serializer = ProductSerializer(instance)
        self.assertEqual(
            set(serializer.data.keys()),
            set(['id', 'name', 'price', 'rating'])
        )
        self.assertEqual(
            serializer.data['name'], 'Headphones')
        self.assertEqual(
            float(serializer.data['rating']), 3)

    def test_create_product_serializer(self):
        product = {
            'name': 'Docking Hub',
            'price': 138.4,
            'rating': 2.8
        }
        serializer = ProductSerializer(data=product)
        serializer.is_valid()

        created_product = serializer.save()
        created_product.refresh_from_db()

        self.assertEqual(created_product.name, 'Docking Hub')

    def test_update_product_serializer(self):
        instance = Product.objects.get(name='Headphones')
        data = {
            'name': 'Headphones',
            'price': 120.4,
            'rating': 4.4
        }
        serializer = ProductSerializer(instance, data=data)
        serializer.is_valid()
        updated_product = serializer.save()
        self.assertEqual(updated_product.name, data['name'])

    def test_partial_update_product_serializer(self):
        instance = Product.objects.get(name='Headphones')
        data = {
            'name': 'Wireless Headphones',
        }
        serializer = ProductSerializer(instance, data=data, partial=True)
        serializer.is_valid()
        updated_product = serializer.save()
        self.assertEqual(updated_product.name, data['name'])
