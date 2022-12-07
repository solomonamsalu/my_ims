from django.shortcuts import render
from .models import Company
from django.views import generic
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

class CompanyList(generic.ListView):
    model=Company
    