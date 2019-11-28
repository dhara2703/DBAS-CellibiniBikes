from django.db import models


# Create your models here.
class MasterInventory(models.Model):
	class Meta:
		db_table = "tblMasterInventory"
		
	inventoryid = models.AutoField(primary_key=True)
	#partid = 
	partname = models.CharField(max_length=100)
	numberofstocks = models.IntegerField()
	parlevel = models.IntegerField()

	

	def __str__(self):
		return str(self.partname)

#only admin can add a new supplier
class Supplier(models.Model):
	class Meta:
		db_table = "tblSupplier"

	supplierid = models.AutoField(primary_key=True)
	suppliername = models.CharField(max_length=30)
	contractstartdate = models.DateTimeField()
	is_active = models.BooleanField(default=True)
	phone =  models.CharField(max_length=16)
	email = models.CharField(max_length=30)


class SupplierOrder(models.Model):
	class Meta:
		db_table = "tblSupplierOrder"

	supplierordernumber = models.AutoField(primary_key=True)
	supplierid = models.ForeignKey(Supplier,on_delete=models.PROTECT)
	date = models.DateTimeField(auto_now_add=True)


class SupplierOrderLineItem(models.Model):
	class Meta:
		db_table = "jncSupplierOrderLineItem"

	supplierordernumber = models.ForeignKey(SupplierOrder, on_delete=models.PROTECT)
	inventoryid = models.ForeignKey(MasterInventory,on_delete=models.PROTECT)
	quantity = models.IntegerField()

class SupplierInvoice(models.Model):
	class Meta:
		db_table = "tblSupplierInvoice"

	supplierinvoiceid = models.AutoField(primary_key=True)	
	supplierinvoicenumber = models.CharField(max_length=16)
	date = models.DateTimeField()
	hst = models.DecimalField(max_digits=3, decimal_places=2)

class SupplierInvoiceLineItem(models.Model):
	class Meta:
		db_table = "jncSupplierInvoiceLineItem"

	supplierinvoicenumber = models.ForeignKey(SupplierInvoice, on_delete=models.PROTECT)
	inventoryid = models.ForeignKey(MasterInventory,on_delete=models.PROTECT)
	quantityshipped = models.IntegerField(default=0)
	price = models.DecimalField(max_digits=8, decimal_places=2) # 999999.99