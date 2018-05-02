from django.contrib.auth.models import User
from django import forms
from .models import Company, Product

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['Name', 'Amount_To_Pay']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Name']