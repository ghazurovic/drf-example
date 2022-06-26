from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        help_text='Name of the product',
        unique=True
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=20,
        help_text='Product price.'
    )
    rating = models.FloatField(
        default=0,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class ProductReview(models.Model):
    class Meta:
        unique_together = ('product', 'user')

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    comment = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )
    product_rating = models.FloatField(
        default=0,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
    )
