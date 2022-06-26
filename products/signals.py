from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg
from .models import ProductReview, Product


def recalc_product_rating(product: Product):
    """Recalculate product rating and save.
    """
    reviews = ProductReview.objects.filter(product=product)
    _rating = reviews.aggregate(Avg('product_rating'))
    product.rating = _rating['product_rating__avg'] \
        if _rating['product_rating__avg'] else 0
    product.save()


@receiver(post_save, sender=ProductReview)
def calculate_product_rating_post_save(sender, instance, created, **kwargs):
    """Calculate rating for product after review has been added.
    """
    recalc_product_rating(instance.product)


@receiver(post_delete, sender=ProductReview)
def calculate_product_rating_post_delete(sender, instance, **kwargs):
    """Calculate rating for product after reviews has been deleted.
    """
    recalc_product_rating(instance.product)
