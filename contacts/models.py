from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.TextField(default=None, null=True)
    mail = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=100, unique=True)