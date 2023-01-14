
from django.db import models
from django.urls import reverse

class Company(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse('company_detail', kwargs={'pk': self.pk})
class Store(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    store_number=models.CharField(max_length=200)
    address=models.TextField()
    def __str__(self) -> str:
        return self.store_number
    def get_absolute_url(self):
        return reverse('store-detail', kwargs={'pk': self.pk})