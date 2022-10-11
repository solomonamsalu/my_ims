from django.shortcuts import render
from django.http import HttpResponse
from .models import Item,Supplier
from django.views import generic
class ItemList(generic.ListView):
    model=Item    
    # template_name='inventory/item_list.html'

