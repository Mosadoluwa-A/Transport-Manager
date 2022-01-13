from django.db import models
from django.contrib.auth.models import User


class Vehicle(models.Model):
    name = models.CharField(max_length=15)
    admin = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="vehicle")

    def __str__(self):
        return self.name


class Passenger(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.BigIntegerField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="passengers")
    created = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
