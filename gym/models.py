from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    equipment_id = models.IntegerField()
    price = models.IntegerField()

    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("gym-details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
    
class Member(models.Model):
    name = models.CharField(max_length=50)
    emailid = models.CharField(max_length=50)
    joindate = models.DateField(max_length=40)
    expiredate = models.DateField(max_length=40)