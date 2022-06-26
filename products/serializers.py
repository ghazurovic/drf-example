from rest_framework import serializers
from .models import Product


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
