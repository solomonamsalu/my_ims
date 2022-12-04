
from django.db import models
from core.models import Store

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    store=models.ForeignKey(Store,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    address=models.TextField()
    def __str__(self) -> str:
        return self.first_name + "  "+ self.last_name