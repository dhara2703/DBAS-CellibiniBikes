from django.shortcuts import render, redirect
from .models import CustomerInvoice, CustomerOrder, CustomerInvoiceLineItem, CustomerOrderLineItem
from .import forms
from django.db import models
from django.apps import apps
from .forms import CustomerOrderForm
from django.forms import modelformset_factory
from django.views.generic import View
Customer = apps.get_model('accounts', 'Customer')
BikesModel = apps.get_model('bike', 'BikeModel')
Bikes = apps.get_model('bike', 'Bike')


# Create your views here.
def homepage(request):
    return render(request, 'customers/customers_homepage.html')


def customerorderlist(request):
    customerorders = CustomerOrder.objects.all()
    return render(request, 'customers/customerorder_list.html', {'customerorders': customerorders})


def customerordercreate(request):
    customers = Customer.objects.all()
    bikes = BikesModel.objects.all()
    if request.method == 'POST':
        orderform = CustomerOrderForm(request.POST)
        if orderform.is_valid():
            customer_order = CustomerOrder()
            customer_order.co_customerid = orderform.cleaned_data['co_customerid']
            customer_order.co_paymentmethod = orderform.cleaned_data['co_paymentmethod']
            customer_order.save()   
            
            bike = Bikes()
            bike.b_modelid = BikesModel.objects.get(bm_modelid=request.POST['coli_bikeid'])
            bike.save()

            print(request.POST['coli_quantity'])

            inlineorder = CustomerOrderLineItem()
            inlineorder.coli_customeroderid = customer_order
            inlineorder.coli_bikeid = bike
            inlineorder.coli_quantity = request.POST['coli_quantity']
            inlineorder.save()

            return render(request, 'customers/customerorder_list.html')
    else:
        form = CustomerOrderForm()
        print("Form is in get")
    return render(request, 'customers/customerorder_create.html', {'customers': customers, 'bikes': bikes})


def customeroderinlinecreate(request, co_customeroderid_id):
    bikes = BikesModel.objects.all()
    inlineorder = CustomerOrder.objects.get(pk=co_customeroderid_id)
    CustomerInvoiceLineItemFormSet = modelformset_factory(
        CustomerOrderLineItem, fields=('coli_bikeid', 'coli_quantity'))
    formset = CustomerInvoiceLineItemFormSet(queryset=CustomerOrderLineItem.objects.filter(co_customeroderid_id=inlineorder.id))
    return redirect(request, 'customers:colist')
