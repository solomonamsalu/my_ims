from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Purchaseorder
from .forms import AddPurchaseForm
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
@method_decorator(login_required, name='dispatch')
class PurchaseorderList(generic.ListView):
    model=Purchaseorder
@method_decorator(login_required, name='dispatch')
class PurchaseorderDetail(generic.DetailView):
    model=Purchaseorder
@method_decorator(login_required, name='dispatch')
class PurchaseorderCreate(generic.CreateView):
    model=Purchaseorder
    fields='__all__'
@method_decorator(login_required, name='dispatch')
class PurchaseorderUpdate(generic.UpdateView):
    model=Purchaseorder
    fields="__all__"
@method_decorator(login_required, name='dispatch')
class PurchaseorderDelete(generic.DeleteView):
    model=Purchaseorder
    success_url=reverse_lazy('purchaseorder_list')

