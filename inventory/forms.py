from django import forms
# from django.forms import ModelForm
from .models import Item
class AddItemForm(forms.ModelForm):
   class Meta:
        model=Item
        fields = "__all__"
        lables={"name":"item_name"}

    # def save(self, commit):
    #     return super().save(commit)
