from django import forms
from django.forms import modelformset_factory
from . import models
from django.forms import Widget


class CustomerOrderForm(forms.ModelForm):
    
    class Meta:
        model = models.CustomerOrder
        fields = ['co_customerid', 'co_paymentmethod', ]
        labels = {
            'co_customerid': 'Customer Name',
            'co_paymentmethod': 'Payment Method',
        }
        
    
    def save(self, commit=True):
        order = super(CustomerOrderForm, self).save(commit=False)
        
        if commit:
            order.save()
        return order
        

class CustomerOrderInlineForm(forms.ModelForm):
    class Meta:
        model = models.CustomerOrderLineItem
        fields = ['coli_bikeid', 'coli_quantity']
        labels = {
            'coli_bikeid': 'Bike Model',
            'coli_quantity': 'Quantity',
        }
        
