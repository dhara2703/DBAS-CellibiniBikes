from django import forms
from django.forms import modelformset_factory
from . import models



class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = models.CustomerOrder
        fields = ['co_customerid', 'co_paymentmethod', ]
        labels = {
            'co_customerid': 'Customer ID',
            'co_paymentmethod': 'Payment Method',
        }
