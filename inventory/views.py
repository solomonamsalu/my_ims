from django.shortcuts import render
from django.http import HttpRequest, HttpResponse,HttpRequest,HttpResponseRedirect
from .models import Item,Supplier
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from .forms import AddItemForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index(request):
    item=Item.objects.all()
    return HttpResponse(item)
def itemcreate(request):
    if request.method=="POST":
        form=AddItemForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=AddItemForm
    return render(request,'inventory/item_create.html',{'form':form})

@method_decorator(login_required, name='dispatch')
class ItemList(generic.ListView):
    model=Item    
class ItemDetail(generic.DetailView):
    model=Item
class SupplierList(generic.ListView):
    model= Supplier  
class SupplierDetail(generic.DetailView):
    model=Supplier

