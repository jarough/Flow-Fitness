from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    equipment_id = models.IntegerField()
    price = models.IntegerField()

    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name