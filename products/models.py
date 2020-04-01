from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    owner = models.ForeignKey(User,
                              related_name="products",
                              on_delete=models.CASCADE,
                              null=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000000, blank=True)
