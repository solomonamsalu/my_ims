from django.db import models
from inventory.models import Supplier,Item
from django.urls import reverse
class Purchaseorder(models.Model):
    STATUS_CHOISES=[
        ('TRANSIT','TRANSIT'),
        ('RECEIVED','RECEIVED'),
    ]
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    deliver_to=models.TextField()
    purchase_order_number=models.CharField(max_length=100)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    rate=models.FloatField()
    amount=models.FloatField(null=True,blank=True)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,choices=STATUS_CHOISES,default='TRANSIT')
    def save(self,*args,**kwargs):
        self.amount=self.quantity*self.rate
        return super().save(*args,**kwargs)
    def __str__(self) -> str:
        return self.purchase_order_number
    def get_absolute_url(self):
        return reverse('purchaseorder_detail',kwargs={'pk':self.pk})





