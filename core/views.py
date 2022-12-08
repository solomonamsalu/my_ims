from django.shortcuts import render
from .models import Company
from django.views import generic
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from .forms import AddCompanyForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import get_object_or_404
class CompanyList(generic.ListView):
    model=Company
def company_create(request):
   if request.method=="POST":
        form=AddCompanyForm(request.POST)
        if form.is_valid():
            form.save()
   else:
        form=AddCompanyForm
   return render(request,'core/company_create.html',{'form':form})
    