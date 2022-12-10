from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Purchaseorder
from .forms import AddPurchaseForm
from django.urls import reverse,reverse_lazy
class PurchaseorderList(generic.ListView):
    model=Purchaseorder
class PurchaseorderDetail(generic.DetailView):
    model=Purchaseorder
class PurchaseorderCreate(generic.CreateView):
    model=Purchaseorder
    fields='__all__'
class PurchaseorderUpdate(generic.UpdateView):
    model=Purchaseorder
    fields="__all__"
class PurchaseorderDelete(generic.DeleteView):
    model=Purchaseorder
    success_url=reverse_lazy('purchaseorder_list')

