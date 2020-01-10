from django.shortcuts import render, redirect
from .models import *
from . import forms
from django import forms as dforms
from django.db.models import Sum
from django.forms import modelformset_factory, formset_factory
import json
from decimal import *
from django.utils import timezone
from .render import Render
from django.views.generic import View
from datetime import datetime
from accounts.models import Employee
from django.contrib.auth.models import User

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
					so_object.soli_supplierordernumber = instance
					so_object.soli_inventoryid = MasterInventory.objects.get(mi_inventoryid=key)
					so_object.soli_quantity = int(quantity)
					so_object.save()

			return redirect('masterInventory:inventoryorderlist')

	else:
		

		io_form = forms.CreateInventoryOrder()


	return render(request, 'inventoryorder/inventoryorder_create.html', {'io_form':io_form, 'partform':partform, 'inventories':inventories})

def inventoryorder_list(request):
	orders = SupplierOrder.objects.filter(so_isreceived=False).order_by('-so_date')
	return render(request, 'inventoryorder/inventoryorder_list.html', {'orders':orders})


def inventoryorder_detail(request, orderid):
	order = SupplierOrder.objects.get(so_supplierordernumber=orderid)
	orderitems = SupplierOrderLineItem.objects.filter(soli_supplierordernumber=orderid)
	return render(request, 'inventoryorder/inventoryorder_detail.html', {'order':order, 'orderitems':orderitems})


#----
#ORDERINVOICE VIEWS
#----
#recieve or approved that an inventory order has been received 
def inventoryinvoice_create(request, orderid):
	order = SupplierOrder.objects.get(so_supplierordernumber=orderid)
	orderitems = SupplierOrderLineItem.objects.filter(soli_supplierordernumber=orderid)

	partform = []
	for orderitem in orderitems:
		partname = {"inventoryid":orderitem.soli_inventoryid.mi_inventoryid,"name":orderitem.soli_inventoryid.mi_partname, "ordered":orderitem.soli_quantity}
		partform.append(partname)


	if request.method == 'POST':
		invoice_form = forms.CreateInventoryInvoice(request.POST)
		print(invoice_form.is_valid())
		if invoice_form.is_valid():
			instance = invoice_form.save(commit=False)
			instance.si_ordernumber = order
			instance.si_date = datetime.now()
			instance.save()

			inventoriesitems = list(SupplierOrderLineItem.objects.filter(soli_supplierordernumber=instance.si_ordernumber).values_list('soli_inventoryid_id', flat=True))

			orderitem = dict(zip(inventoriesitems, request.POST.getlist('orderitem')))
			for key, quantity in orderitem.items():
				inventoryitem = MasterInventory.objects.get(mi_inventoryid=key)
				sili_object = SupplierInvoiceLineItem(sili_supplierinvoicenumber=instance, sili_inventoryid=inventoryitem, sili_quantityshipped=int(quantity))
				sili_object.calculateprice()
				sili_object.save()
				sili_object.updatestock()

			return redirect('masterInventory:inventoryinvoicelist')

	else:
		invoice_form = forms.CreateInventoryInvoice()

	return render(request, 'inventoryinvoice/inventoryinvoice_create.html', {'order':order, 'invoice_form':invoice_form, 'partform':partform})

def inventoryinvoice_list(request):
	orders = SupplierInvoice.objects.all().order_by('si_date')
	return render(request, 'inventoryinvoice/inventoryinvoice_list.html', {'orders':orders})

def inventoryinvoice_detail(request, invoiceid):
	order = SupplierInvoice.objects.get(si_supplierinvoiceid=invoiceid) #its actually invoice number
	orderitems = SupplierInvoiceLineItem.objects.filter(sili_supplierinvoicenumber=order.si_supplierinvoiceid)
	subtotal = 0
	for item in orderitems:
		 subtotal += Decimal(item.sili_quantityshipped) * item.sili_inventoryid.mi_price

	total = (Decimal(1) + order.si_hst) * subtotal
	total = "{:.2f}".format(total)
	
	return render(request, 'inventoryinvoice/inventoryinvoice_detail.html', {'order':order, 'orderitems':orderitems,'subtotal':subtotal, 'total':total})

#----
#SUPPLIER VIEWS
#----
def supplier_list(request):
	suppliers = Supplier.objects.filter(s_is_active=1)
	return render(request, 'supplier/supplier_list.html', {'suppliers':suppliers})

#----
#DEFECTS VIEWS
#----

def defects_list(request):
	defects = Defect.objects.values('d_supplierinvoicenumber__si_supplierinvoicenumber').annotate(totalquantity=Sum('d_quantity'))
	return render(request, 'defect/defects_list.html', {'defects':defects})

def defect_detail(request, defectinvoiceid):
	invoice = SupplierInvoice.objects.get(si_supplierinvoicenumber=defectinvoiceid)
	defects = Defect.objects.filter(d_supplierinvoicenumber=invoice)
	return render(request, 'defect/defects_detail.html', {'defects':defects,'defectinvoiceid':defectinvoiceid})

def defect_create(request, invoiceid):
	invoice = SupplierInvoice.objects.get(si_supplierinvoiceid=invoiceid)
	receiveditems = SupplierInvoiceLineItem.objects.filter(sili_supplierinvoicenumber=invoice)
	partselection = []
	print(request.user.id)

	for receiveditem in receiveditems:
		partname = {"id":receiveditem.sili_inventoryid.mi_inventoryid, "name":receiveditem.sili_inventoryid.mi_partname}
		partselection.append(partname)

	if request.method == 'POST':
		defect_form = forms.ReportDefects(request.POST)
		if (defect_form.is_valid()):
			instance = defect_form.save(commit=False)
			instance.d_inventoryid = MasterInventory.objects.get(mi_inventoryid=request.POST['part'])
			instance.d_supplierinvoicenumber = invoice
			instance.d_employeeid = Employee.objects.get(e_userid=request.user.id)   
			instance.d_date = datetime.now()
			instance.save()
			instance.updatestock()
			return redirect('masterInventory:defectslist')
	else:
		defect_form = forms.ReportDefects()

	return render(request, 'defect/defects_create.html', {'defect_form':defect_form, 'invoice':invoice, 'partselection':partselection})

#REPORT VIEWS

def pdforder(request, orderid):
	today = timezone.now()
	order = SupplierOrder.objects.get(so_supplierordernumber=orderid)
	orderitems = SupplierOrderLineItem.objects.filter(soli_supplierordernumber=orderid)
	return Render.render('inventoryorder/inventoryorder_report.html', {'today':today,'order':order, 'orderitems':orderitems} )

def Pdfinventory(request):
    today = timezone.now()
    inventories = MasterInventory.objects.all().order_by('mi_inventoryid')
    return Render.render('masterinventory/inventory_report.html', {'today':today, 'inventories':inventories})

def pdfinvoice(request, invoiceid):
	today = timezone.now()
	order = SupplierInvoice.objects.get(si_supplierinvoiceid=invoiceid) #its actually invoice number
	orderitems = SupplierInvoiceLineItem.objects.filter(sili_supplierinvoicenumber=order.si_supplierinvoiceid)
	subtotal = 0
	for item in orderitems:
		 subtotal += Decimal(item.sili_quantityshipped) * item.sili_price

	total = (Decimal(1) + order.si_hst) * subtotal
	total = "{:.2f}".format(total)

	return Render.render('inventoryinvoice/inventoryinvoice_report.html', {'today':today,'order':order, 'orderitems':orderitems,'subtotal':subtotal,'total':total})


    