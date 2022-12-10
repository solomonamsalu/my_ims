from django.shortcuts import render
from django.http import HttpRequest, HttpResponse,HttpRequest,HttpResponseRedirect
from .models import Item,Supplier
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from .forms import AddItemForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

def index(request):
    item=Item.objects.all()
    return HttpResponse(item)


@method_decorator(login_required, name='dispatch')
class ItemCreate(generic.CreateView):
    model=Item
    fields='__all__'
@method_decorator(login_required, name='dispatch')
class ItemUpdate(generic.UpdateView):
    model=Item
    fields="__all__"
@method_decorator(login_required, name='dispatch')
class ItemDelete(generic.DeleteView):
    model=Item
    success_url=reverse_lazy('item_list')
@method_decorator(login_required, name='dispatch')
class ItemList(generic.ListView):
    model=Item    
@method_decorator(login_required, name='dispatch')
class ItemDetail(generic.DetailView):
    model=Item
@method_decorator(login_required, name='dispatch')
class SupplierList(generic.ListView):
    model= Supplier 
@method_decorator(login_required, name='dispatch')
class SupplierDetail(generic.DetailView):
    model=Supplier
@method_decorator(login_required, name='dispatch')
class SupplierCreate(generic.CreateView):
    model=Supplier
    fields='__all__'
@method_decorator(login_required, name='dispatch')
class SupplierUpdate(generic.UpdateView):
    model=Supplier
    fields="__all__"
@method_decorator(login_required, name='dispatch')
class SupplierDelete(generic.DeleteView):
    model=Supplier
    success_url=reverse_lazy('supplier_list')
