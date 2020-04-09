from django.db import models
from django.contrib.auth.models import User


class ProductType(models.Model):
    title = models.CharField(null=False, max_length=160)
    description = models.TextField(default="")


# Create your models here.
class Product(models.Model):
    owner = models.ForeignKey(User,
                              related_name="products",
                              on_delete=models.CASCADE,
                              null=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000000, blank=True)
    typeId = models.ForeignKey(ProductType, null=True, on_delete=models.SET_NULL)
    image = models.TextField(default=None, null=True)
