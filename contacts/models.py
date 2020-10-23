from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.TextField(default=None, null=True)
    mail = models.CharField(max_length=100, unique=True)
    role = models.TextField(max_length=100, null=True)
    priority = models.IntegerField(default=-1, null=False)

    def load_role(self):
        print(self.role)
        if self.role:
            import json
            loads = self.role
            try:
                loads = json.loads(self.role)
            except:
                pass
            return loads
        return None
