from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, primary_key=True)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100, null=True)
    post_code = models.CharField(max_length=100)

    def __str__(self):
        return self.slug
