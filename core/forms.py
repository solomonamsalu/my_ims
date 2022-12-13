from django import forms
from .models import Company,Store
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ("username","email")
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
class AddCompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields = ['name']
class AddStoreForm(forms.ModelForm):
    class Meta:
        model=Store
        fields='__all__'
        