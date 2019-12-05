from django.shortcuts import render, redirect
from .models import *
from . import forms
from django import forms as dforms
from django.db.models import Sum
from django.forms import modelformset_factory
from django.forms import formset_factory
import json
from django.db.models import Sum
from decimal import *
from django.utils import timezone
from .render import Render
from django.views.generic import View

def inventory_list(request):
	inventories = MasterInventory.objects.all().order_by('mi_inventoryid')
	return render(request, 'masterinventory/inventory_list.html', {'inventories':inventories})

#only super user and sales should have access to this
def inventory_item_create(request):
	if request.method =='POST':
		form = forms.CreateQuote(request.POST)
		if form.is_valid():
			#save article to db
			instance = form.save(commit=False)
			instance.save()
			return redirect('masterInventory:inventorylist')
	else:
		form = forms.CreateInventoryItem()

	return render(request, 'masterinventory/inventory_create.html', {'form': form})

#----
#ORDERINVENTORY VIEWS
#----

def inventoryorder_list(request):
	orders = SupplierOrder.objects.all().order_by('-so_date')
	return render(request, 'inventoryorder/inventoryorder_list.html', {'orders':orders})

def inventoryorder_detail(request, orderid):
	order = SupplierOrder.objects.get(so_supplierordernumber=orderid)
	orderitems = SupplierOrderLineItem.objects.filter(soli_supplierordernumber=orderid)
	return render(request, 'inventoryorder/inventoryorder_detail.html', {'order':order, 'orderitems':orderitems})

def inventoryorder_create(request):
	inventories = MasterInventory.objects.all().order_by('mi_inventoryid')
	numberofinventory = MasterInventory.objects.all().count()
	partform = []
	for inventory in inventories:
		partname = {"name":inventory.mi_partname, "par":inventory.mi_parlevel, "onhand":inventory.mi_numberofstocks}
		partform.append(partname)
	if request.method == 'POST':
		io_form = forms.CreateInventoryOrder(request.POST)
		if io_form.is_valid():
			instance = io_form.save(commit=False)
			instance.save()

			inventoriesitems = list(MasterInventory.objects.values_list('mi_inventoryid', flat=True))
			print(request.POST.getlist('orderitem'))

			orderitem = dict(zip(inventoriesitems, request.POST.getlist('orderitem')))
			for key, quantity in orderitem.items():
				if int(quantity) > 0:
					so_object = SupplierOrderLineItem()
					so_object.soli_supplierordernumber = instance.so_supplierordernumber
					so_object.soli_inventoryid = key
					so_object.soli_quantity = int(quantity)
					so_object.save()

			return redirect('masterInventory:inventoryorderlist')

	else:
		

		io_form = forms.CreateInventoryOrder()


	return render(request, 'inventoryorder/inventoryorder_create.html', {'io_form':io_form, 'partform':partform, 'inventories':inventories})

#----
#ORDERINVOICE VIEWS
#----
def inventoryinvoice_list(request):
	orders = SupplierInvoice.objects.all().order_by('si_date')
	return render(request, 'inventoryinvoice/inventoryinvoice_list.html', {'orders':orders})

def inventoryinvoice_detail(request, invoiceid):
	order = SupplierInvoice.objects.get(si_supplierinvoiceid=invoiceid) #its actually invoice number
	orderitems = SupplierInvoiceLineItem.objects.filter(sili_supplierinvoicenumber=order.si_supplierinvoiceid)
	subtotal = 0
	for item in orderitems:
		 subtotal += Decimal(item.sili_quantityshipped) * item.sili_price

	total = (Decimal(1) + order.si_hst) * subtotal
	total = "{:.2f}".format(total)
	
	return render(request, 'inventoryinvoice/inventoryinvoice_detail.html', {'order':order, 'orderitems':orderitems,'subtotal':subtotal, 'total':total})
#----
#DEFECTS VIEWS
#----

def supplier_list(request):
	suppliers = Supplier.objects.filter(s_is_active=1)
	return render(request, 'supplier/supplier_list.html', {'suppliers':suppliers})

def defects_list(request):
	#defects = Defect.objects.all()
	defects = Defect.objects.values('d_supplierordernumber__so_supplierordernumber').count()
	return render(request, 'defect/defects_list.html', {'defects':defects})

def defect_detail(request, defectid):
	defect = Defect.object.get(d_defectid=defectid)
	return render(request, 'defect/defect_detail.html', {'defect':defect})

# def create_defect(request):
	# return something


class Pdfinventory(View):

    def get(self, request):
        today = timezone.now()
        inventories = MasterInventory.objects.all().order_by('mi_inventoryid')
        return Render.render('masterinventory/inventory_report.html', {'today':today, 'inventories':inventories})

class Pdforder(View):

    def get(self, request, orderid):
        order = SupplierOrder.objects.get(so_supplierordernumber=orderid)
        orderitems = SupplierOrderLineItem.objects.filter(soli_supplierordernumber=orderid)
        return Render.render('masterinventory/inventory_report.html', {'order':order, 'orderitems':orderitems})