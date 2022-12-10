from django import forms
from .models import Company,Store
class AddCompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields = ['name']
class AddStoreForm(forms.ModelForm):
    class Meta:
        model=Store
        fields='__all__'
        