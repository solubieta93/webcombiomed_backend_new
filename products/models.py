from django.db import models
from django.contrib.auth.models import User


class ProductType(models.Model):
    title = models.CharField(null=False, max_length=100)
    description = models.TextField(default="")
    image = models.TextField(default=None, null=True)
    priority = models.IntegerField(default=-1, null=False)

    def load_title(self):
        if self.title:
            loads = self.title
            import json
            try:
                loads = json.loads(self.title)
            except:
                pass
            return loads
        return None

    def load_description(self):
        if self.title:
            loads = self.description
            import json
            try:
                loads = json.loads(self.description)
            except:
                pass
            return loads
        return None


# Create your models here.
class Product(models.Model):
    owner = models.ForeignKey(User,
                              related_name="products",
                              on_delete=models.CASCADE,
                              null=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, blank=True)
    typeId = models.ForeignKey(ProductType, null=True, on_delete=models.SET_NULL)
    image = models.TextField(default=None, null=True)
    defaultImage = models.IntegerField(default=-1, null=True)
    json_images = models.TextField(default=None, null=True)
    json_details = models.TextField(default=None, null=True)
    json_files = models.TextField(default=None, null=True)

    def load_images(self):
        if self.json_images:
            import json
            loads = [self.json_images]
            try:
                loads = json.loads(self.json_images)
            except:
                pass
            print(loads)
            return loads
        return None

    def load_details(self):
        if self.json_details:
            import json
            return json.loads(self.json_details)
        return None

    def load_files(self):
        if self.json_files:
            import json
            return json.loads(self.json_files)
        return None
