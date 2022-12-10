from django import forms
from django.forms import ModelForm
from .models import Salesorder,Customer
class AddSalesForm(forms.ModelForm):
    class Meta:
        model=Salesorder
        fields=('__all__')
class AddCustomerForm(forms.ModelForm):
    class Meta:
        mode=Customer
        fields=('__all__')

