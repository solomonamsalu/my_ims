from django.shortcuts import render
from .models import Company,Store
from django.views import generic
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from .forms import AddCompanyForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
@method_decorator(login_required, name='dispatch')
class CompanyList(generic.ListView):
    model=Company
class CompanyDetail(generic.DetailView):
   model=Company
class CompanyCreate(generic.CreateView):
   model=Company
   fields='__all__'
class CompanyUpdate(generic.UpdateView):
   model=Company
   fields='__all__'
   # success_url=reverse_lazy('company_detail')
class CompanyDelete(generic.DeleteView):
   model=Company
   success_url=reverse_lazy('company_list')
class StoreList(generic.ListView):
    model=Store
class StoreDetail(generic.DetailView):
   model=Store
class StoreCreate(generic.CreateView):
   model=Store
   fields='__all__'
class StoreUpdate(generic.UpdateView):
   model=Store
   fields='__all__'
   # success_url=reverse_lazy('store_detail')
class StoreDelete(generic.DeleteView):
   model=Store
   success_url=reverse_lazy('store_list')