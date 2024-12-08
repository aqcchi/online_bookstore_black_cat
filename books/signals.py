from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order


@receiver(post_save, sender=Order)
def update_total_sales(sender, instance, **kwargs):
    if instance.is_completed:
        from django.core.cache import cache
        total_sales = cache.get('total_sales', 0)
        total_sales += instance.amount_paid
        cache.set('total_sales', total_sales)


