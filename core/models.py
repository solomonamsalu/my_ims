
from django.db import models

class Company(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class Store(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    store_number=models.CharField(max_length=200)
    address=models.TextField()