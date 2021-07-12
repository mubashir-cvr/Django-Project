
from django.db import models


# Create your models here.
class Users(models.Model):
    id = int
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics', blank=True)
    desc = models.TextField()

    def _name_(self):
        return self.name


class Service(models.Model):
    id = int
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics', blank=True)
    cost = models.BigIntegerField()
    ServiceType = models.CharField(max_length=100)
    ServiceSubType = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"{self.name}"


class Servicer(models.Model):
    id = int
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics', blank=True)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    isActive = models.BooleanField(default=True)
    pendingJob = models.IntegerField(default=0)
    numberofJob = models.IntegerField(default=0)
    rating = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return f"{self.name}"
