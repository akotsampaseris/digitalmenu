from django.db import models

from shops.models import Shop

# Create your models here.
class Menu(models.Model):
    LANGUAGES = [
    ('GR', 'Greek'),
    ('EN', 'English'),
    ('DE', 'German'),
    ('SP', 'Spanish'),
    ('IT', 'Italian'),
    ('RS', 'Russian'),
    ('CH', 'Chinese')
    ]

    CURRENCIES = [
        ('EUR', 'Euro'),
        ('USD', 'US Dollar'),
        ('GBP', 'UK Pound')
    ]

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='GR')
    currency = models.CharField(max_length=3, choices=CURRENCIES, default='EUR')


class MenuCategory(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
