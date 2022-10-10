from enum import unique
from django.db import models

from core.models import Company

class Supplier(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True,related_name='suppliers')
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200,unique=True)
    phone=models.CharField(max_length=200,unique=True)
    address=models.TextField()
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name