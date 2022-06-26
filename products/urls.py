from rest_framework.routers import DefaultRouter
from .views import ProductsViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')

products_api = [
    path('', include(router.urls)),
]
