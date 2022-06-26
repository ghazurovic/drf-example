from rest_framework.routers import DefaultRouter
from .views import ProductsViewSet, ProductReviewsViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')
router.register(
    r'product-reviews',
    ProductReviewsViewSet,
    basename='product-reviews'
)

products_api = [
    path('', include(router.urls)),
]
