
from django.db import models
from core.models import Store
from inventory.models import Item

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    store=models.ForeignKey(Store,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    address=models.TextField()
    def __str__(self) -> str:
        return self.first_name + "  "+ self.last_name
class Salesorder(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE,default='null')
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    sales_order_number=models.CharField(max_length=100)
    store=models.ForeignKey(Store,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    rate=models.FloatField()
    amount=models.FloatField(null=True,blank=True)
    date=models.DateField(auto_now_add=True)
    def save(self,*args,**kwargs):
        self.amount=self.quantity*self.rate
        return super().save(*args,**kwargs)
    def __str__(self) -> str:
        return self.sales_order_number