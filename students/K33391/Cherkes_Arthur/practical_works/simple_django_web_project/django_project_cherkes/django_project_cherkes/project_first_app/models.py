from django.db import models
from django.contrib.auth.models import AbstractUser
from django_project_cherkes import settings


# Create your models here.


class Owner(AbstractUser):
    owner_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)
    passport = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=20, blank=True, null=True)


class DriverLicense(models.Model):
    license_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    registration_date = models.DateField()


class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    owners = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ownership')

class Ownership(models.Model):
    ownership_id = models.IntegerField(primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=False)