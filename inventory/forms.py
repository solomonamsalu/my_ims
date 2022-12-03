from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from .models import Item
class AddItemForm(forms.ModelForm):
   class Meta:
        model=Item
        fields = "__all__"
        widgets = {
        'name': TextInput(attrs={
            'class': "form-control"
            }),
        'sku_number':TextInput(attrs={
            'class': "form-control"
            }),
        'selling_price':TextInput(attrs={
            'class': "form-control"
            }),
        'cost_price':TextInput(attrs={
            'class': "form-control"
            }),
        'max_stock':TextInput(attrs={
            'class': "form-control"
            }),
        'onhand_stock':TextInput(attrs={
            'class': "form-control"
            }),
        'reorder_point':TextInput(attrs={
            'class': "form-control"
            }),
        'priferred_supplier':TextInput(attrs={
            'class': "form-control"
            })
            }

