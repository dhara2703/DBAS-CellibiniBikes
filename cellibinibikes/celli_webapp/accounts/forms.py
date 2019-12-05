from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models
from .models import Employee, Customer
from django.forms import modelformset_factory


class DefaultUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'email',
                  'first_name', 'last_name',
                  'password1', 'password2')

    def save(self, commit=True):
        user = super(DefaultUserForm, self).save(commit=False)
        user.is_staff = True
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class CreateEmployeeAccountForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['e_streetaddress1', 'e_streetaddress2', 'e_city', 'e_province', 'e_postalcode',
                  'e_country', 'e_phonenumber', 'e_salary', 'e_startdate', 'e_sinnumber', 'e_isapprentice'
                  ]
        labels = {
            'e_streetaddress1': 'Street Address1',
            'e_streetaddress2': 'Street Address2',
            'e_city': 'City',
            'e_province': 'Province',
            'e_postalcode': 'Postal Code',
            'e_country': 'Country',
            'e_phonenumber': 'Phone Number',
            'e_salary': 'Salary',
            'e_startdate': 'Start Date',
            'e_sinnumber': 'SIN Number',
            'e_isapprentice': 'Is Apprentice',
        }


class CustomerUserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'email',
                  'first_name', 'last_name')
        labels = {
            'username': 'User Name',
            'email': 'Email Address',
            'first_name': 'Email Address',
            'last_name': 'Last Name',
        }

    def save(self, commit=True):
        user = super(CustomerUserForm, self).save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class CreateCustomerAccountForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['c_streetaddress1', 'c_streetaddress2', 'c_city', 'c_province', 'c_postalcode',
                  'c_country', 'c_phonenumber', 'c_issubscribed', 'c_companyname'
                  ]
        labels = {
            'c_streetaddress1': 'Street Address1',
            'c_streetaddress2': 'Street Address2',
            'c_city': 'City',
            'c_province': 'Province',
            'c_postalcode': 'Postal Code',
            'c_country': 'Country',
            'c_phonenumber': 'Phone Number',
            'c_issubscribed': 'Is Subscrbed User',
            'c_companyname': 'Company Name'
        }

