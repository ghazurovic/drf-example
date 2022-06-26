from rest_framework import serializers
from .models import Product, ProductReview


class ProductSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'rating',
        )


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'
