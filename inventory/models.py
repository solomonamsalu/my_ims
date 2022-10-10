from django.db import models

# Create your models here.class Customer(models.Model):
class Customer(models.Model):
    name=models.CharField(max_length=200)
class Vihicle(models.Model):
    name=models.CharField(max_length=200)
    customers=models.ManyToManyField(Customer)
    price=models.IntegerField()
