from django.db import models

# Create your models here.
class Shop(models.Model):
    is_active = models.BooleanField(default=True)
    slug = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100, null=True)
    post_code = models.CharField(max_length=100)

    def __str__(self):
        return self.slug
