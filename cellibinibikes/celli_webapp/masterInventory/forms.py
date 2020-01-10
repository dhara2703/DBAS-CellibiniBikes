from django import forms
from django.forms import modelformset_factory
from . import models


class CreateInventoryItem(forms.ModelForm):
	class Meta:
		model = models.MasterInventory
		fields = ['mi_partname', 'mi_numberofstocks', 'mi_parlevel']
		#add restrictions for input later


class CreateInventoryOrder(forms.ModelForm):
	class Meta:
		model = models.SupplierOrder
		fields = ['so_supplierid']


InventoryItemFormset = modelformset_factory(
	models.SupplierOrderLineItem, fields=('soli_inventoryid', 'soli_quantity',))


class CreateOrderLineItem(forms.ModelForm):
	class Meta:
		model = models.SupplierOrderLineItem
		fields = ['soli_quantity']
		# labels = {
  #                   'soli_quantity': nameofPart
		# }
		widgets = {'soli_quantity': forms.IntegerField()}


class CreateInventoryInvoice(forms.ModelForm):
	class Meta:
		model = models.SupplierInvoice
		fields = ['si_supplierinvoicenumber']
		labels ={'si_supplierinvoicenumber':'Supplier Invoice Number'}

class ReportDefects(forms.ModelForm):
	class Meta:
		model = models.Defect
		fields = ['d_quantity', 'd_defectdesc']
		labels= {
		'd_quantity':'Quantity',
		'd_defectdesc':'description'
		}
		widgets = {
		'd_defectdesc': forms.Textarea(attrs={"rows":5, "cols":20})
		}