from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Shop, ShopWebInfo, ShopAddressInfo

@receiver(post_save, sender=Shop)
def create_shop_web_info(sender, instance, created, **kwargs):
    print('Shop created')
    if created:
        ShopWebInfo.objects.create(shop=instance)


@receiver(post_save, sender=Shop)
def create_shop_address_info(sender, instance, created, **kwargs):
    print('Shop created')
    if created:
        ShopAddressInfo.objects.create(shop=instance)
