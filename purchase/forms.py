from django import forms
from django.forms import ModelForm
from .models import Purchaseorder
class AddPurchaseForm(forms.ModelForm):
    class Meta:
        model=Purchaseorder
        fields=('__all__')


