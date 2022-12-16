from enum import unique
from django.db import models

from core.models import Company,Store
from django.urls import reverse

class Supplier(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True,related_name='suppliers')
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200,unique=True)
    phone=models.CharField(max_length=200,unique=True)
    address=models.TextField()
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    def get_absolute_url(self):
        return reverse('supplier_detail', kwargs={'pk': self.pk})
class Item(models.Model):
    name=models.CharField(max_length=200)
    store=models.ForeignKey(Store,on_delete=models.CASCADE, null=True,blank=True,related_name='items')
    sku_number=models.CharField(max_length=200)
    selling_price=models.FloatField()
    cost_price=models.FloatField()
    max_stock=models.IntegerField()
    onhand_stock=models.IntegerField()
    reorder_point=models.IntegerField()
    preferred_supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE,related_name='items')
    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse('item_detail',kwargs={ 'pk':self.pk})