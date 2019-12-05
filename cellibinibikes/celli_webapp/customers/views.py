from django.shortcuts import render, redirect
from .models import CustomerOrder, CustomerOrderLineItem, CustomerInvoice, CustomerInvoiceLineItem
from .import forms

# Create your views here.


def homepage(request):
      return render(request, 'customers/customers_homepage.html')


def customerorder_list(request):
      return render(request, 'customers/customerorder_list.html')


def customerorder_create(request):
      if request.method == 'POST':
            customerorderform = forms.CustomerOrderForm(request.POST)
            if customerorderform.is_valid():
                  customerorderinstance = customerorderform.save()
              
      return render(request, 'customers/customerorder_list.html')
