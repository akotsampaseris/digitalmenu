from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User

# Create your models here.
class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    category = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ShopWebInfo(models.Model):
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE, primary_key=True)
    website = models.URLField(max_length=100, blank=True)
    fb_page = models.URLField(max_length=100, blank=True)
    instagram_page = models.URLField(max_length=100, blank=True)
    trip_advisor_page = models.URLField(max_length=100, blank=True)


class ShopAddressInfo(models.Model):
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    address_1 = models.CharField(max_length=100, blank=True)
    address_2 = models.CharField(max_length=100, blank=True)
    post_code = models.CharField(max_length=100, blank=True)


@receiver(post_save, sender=Shop)
def create_shop_web_info(sender, instance, created, **kwargs):
    print('Shop created')
    print(instance)
    if created:
        ShopWebInfo.objects.create(shop=instance)


@receiver(post_save, sender=Shop)
def create_shop_address_info(sender, instance, created, **kwargs):
    print('Shop created')
    print(instance)
    if created:
        ShopAddressInfo.objects.create(shop=instance)
