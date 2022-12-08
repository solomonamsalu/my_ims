from django.shortcuts import render
from .models import Company
from django.views import generic
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from .forms import AddCompanyForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
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