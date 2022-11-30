from django.shortcuts import render
from django.http import HttpRequest, HttpResponse,HttpRequest
from .models import Item,Supplier
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

def index(request):
    item=Item.objects.all()
    return HttpResponse(item)

class ItemList(generic.ListView):
    model=Item    
class ItemDetail(generic.DetailView):
    model=Item

    