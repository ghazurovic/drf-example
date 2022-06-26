from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'rating'
        )

    def validate_rating(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError('Rating has to be between 1 and 10.')
        return value
