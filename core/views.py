from django.shortcuts import render,redirect
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
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("company_list")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="core/register.html", context={"form":form})
@method_decorator(login_required, name='dispatch')
class CompanyList(generic.ListView):
    model=Company
@method_decorator(login_required, name='dispatch')
class CompanyDetail(generic.DetailView):
   model=Company
@method_decorator(login_required, name='dispatch')
class CompanyCreate(generic.CreateView):
   model=Company
   fields='__all__'
@method_decorator(login_required, name='dispatch')
class CompanyUpdate(generic.UpdateView):
   model=Company
   fields='__all__'
@method_decorator(login_required, name='dispatch')
class CompanyDelete(generic.DeleteView):
   model=Company
   success_url=reverse_lazy('company_list')
@method_decorator(login_required, name='dispatch')
class StoreList(generic.ListView):
    model=Store
@method_decorator(login_required, name='dispatch')
class StoreDetail(generic.DetailView):
   model=Store
@method_decorator(login_required, name='dispatch')
class StoreCreate(generic.CreateView):
   model=Store
   fields='__all__'
@method_decorator(login_required, name='dispatch')
class StoreUpdate(generic.UpdateView):
   model=Store
   fields='__all__'
@method_decorator(login_required, name='dispatch')
class StoreDelete(generic.DeleteView):
   model=Store
   success_url=reverse_lazy('store_list')