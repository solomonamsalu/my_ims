from django.shortcuts import render
from .models import Customer,Salesorder
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.urls import reverse,reverse_lazy
@method_decorator(login_required, name='dispatch')
class SalesorderList(generic.ListView):
    model=Salesorder
@method_decorator(login_required, name='dispatch')
class SalesorderDetail(generic.DetailView):
    model=Salesorder
@method_decorator(login_required, name='dispatch')
class SalesorderCreate(generic.CreateView):
    model=Salesorder
    fields='__all__'
@method_decorator(login_required, name='dispatch')
class SalesorderUpdate(generic.UpdateView):
    model=Salesorder
    fields="__all__"
@method_decorator(login_required, name='dispatch')
class SalesorderDelete(generic.DeleteView):
    model=Salesorder
    success_url=reverse_lazy('purchaseorder_list')
@method_decorator(login_required, name='dispatch')
class CustomerList(generic.ListView):
    model=Customer
@method_decorator(login_required, name='dispatch')
class CustomerDetail(generic.DetailView):
    model=Customer
@method_decorator(login_required, name='dispatch')
class CustomerCreate(generic.CreateView):
    model=Customer
    fields='__all__'
@method_decorator(login_required, name='dispatch')
class CustomerUpdate(generic.UpdateView):
    model=Customer
    fields="__all__"
@method_decorator(login_required, name='dispatch')
class CustomerDelete(generic.DeleteView):
    model=Customer
    success_url=reverse_lazy('customer_list')
