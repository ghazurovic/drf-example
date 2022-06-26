import json
from django.test import TestCase
from products.serializers import ProductSerializer
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from products.models import Product


client = APIClient()


class GetProducts(TestCase):
    """ Test list"""
    def setUp(self):
        Product.objects.bulk_create([
            Product(name='Headphones', price=200.30, rating=3),
            Product(name='Keyboard', price=179, rating=4),
            Product(name='Notebook', price=3799, rating=5),
            Product(name='Display', price=450, rating=1),
            Product(name='Table', price=1850, rating=2)
        ])

    def test_get_all_products(self):
        response = client.get(reverse('products-list'))
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(len(response.data), len(serializer.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateProductTest(TestCase):
    """ Test create """
    def setUp(self):
        self.payload = {
            'name': 'Keyboard',
            'price': 180,
            'rating': 3
        }
        self.invalid_payload = {
            'name': 'Keyboard',
            'price': 'str__',
            'rating': '2'
        }

    def test_create_product(self):
        response = client.post(
            '/api/products/',
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_product(self):
        response = client.post(
            '/api/products/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteProductTest(TestCase):
    """ Test delete """

    def setUp(self):
        self.headphones = Product.objects.create(
            name='Headphones', price=200.30, rating=3
        )

    def test_delete(self):
        response = client.delete(
            f'/api/products/{self.headphones.pk}/',
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class UpdateProductTest(TestCase):
    """ Test update """
    def setUp(self):
        self.headphones = Product.objects.create(
            name='Headphones', price=200.30, rating=3
        )
        self.keyboard = Product.objects.create(
            name='Keyboard', price=179, rating=4
        )
        self.payload = {
            'name': 'Wireless Headphones',
            'price': 160,
            'rating': 4.9
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_update_product(self):
        response = client.put(
            f'/api/products/{self.headphones.pk}/',
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_product(self):
        response = client.put(
            f'/api/products/{self.headphones.pk}/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
