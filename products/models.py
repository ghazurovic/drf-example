from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
