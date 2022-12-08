from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from .models import Item
class AddItemForm(forms.ModelForm):
   class Meta:
        model=Item
        fields = '__all__'
        
