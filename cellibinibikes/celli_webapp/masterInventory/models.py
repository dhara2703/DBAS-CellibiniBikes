from django.db import models
from decimal import Decimal


# Create your models here.
class MasterInventory(models.Model):
	class Meta:
		db_table = "tblMasterInventory"
		
	mi_inventoryid = models.AutoField(primary_key=True)
	#partid = 
	mi_partname = models.CharField(max_length=100)
	mi_numberofstocks = models.IntegerField()
	mi_parlevel = models.IntegerField()
	mi_price = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal('00000.00'))


	def __str__(self):
		return str(self.mi_partname)

	def updatestock(self, received):
		self.mi_numberofstocks += received
		self.save()

#only admin can add a new supplier
class Supplier(models.Model):
	class Meta:
		db_table = "tblSupplier"

	s_supplierid = models.AutoField(primary_key=True)
	s_suppliername = models.CharField(max_length=30)
	s_companyname = models.CharField(max_length=100, blank=True, null=True,default="")
	s_contractstartdate = models.DateTimeField()
	s_is_active = models.BooleanField(default=True)
	s_phone =  models.CharField(max_length=16)
	s_email = models.CharField(max_length=30)

	def __str__(self):
		return str(self.s_companyname)

class SupplierOrder(models.Model):
	class Meta:
		db_table = "tblSupplierOrder"

	so_supplierordernumber = models.AutoField(primary_key=True)
	so_supplierid = models.ForeignKey(Supplier, on_delete=models.PROTECT)
	so_date = models.DateTimeField(auto_now_add=True)
	so_isreceived = models.BooleanField(default=False)

	def orderreceived(self):
		self.so_isreceived = True
		self.save()

class SupplierOrderLineItem(models.Model):
	class Meta:
		db_table = "jncSupplierOrderLineItem"

	soli_supplierordernumber = models.ForeignKey(SupplierOrder, on_delete=models.PROTECT)
	soli_inventoryid = models.ForeignKey(MasterInventory,on_delete=models.PROTECT)
	soli_quantity = models.IntegerField()

class SupplierInvoice(models.Model):
	class Meta:
		db_table = "tblSupplierInvoice"

	si_supplierinvoiceid = models.AutoField(primary_key=True)	
	si_supplierinvoicenumber = models.CharField(max_length=16)
	si_ordernumber = models.ForeignKey(SupplierOrder, on_delete=models.PROTECT)
	si_date = models.DateTimeField()
	si_hst = models.DecimalField(max_digits=3, decimal_places=2, default=Decimal('0.13'))

	def __str__(self):
		return str(self.si_supplierinvoiceid)

	def received(self):
		self.si_ordernumber.orderreceived()

class SupplierInvoiceLineItem(models.Model):
	class Meta:
		db_table = "jncSupplierInvoiceLineItem"

	sili_supplierinvoicenumber = models.ForeignKey(SupplierInvoice, on_delete=models.PROTECT)
	sili_inventoryid = models.ForeignKey(MasterInventory,on_delete=models.PROTECT)
	sili_quantityshipped = models.IntegerField(default=0)
	sili_price = models.DecimalField(max_digits=8, decimal_places=2)  # 999999.99

	def updatestock(self):
		inventory = MasterInventory.objects.get(mi_inventoryid = str(self.sili_inventoryid.mi_inventoryid))
		inventory.updatestock(self.sili_quantityshipped)


	def calculateprice(self):
		inventory = MasterInventory.objects.get(mi_inventoryid = str(self.sili_inventoryid.mi_inventoryid))
		self.sili_price = inventory.mi_price * self.sili_quantityshipped	

class Defect(models.Model):
    class Meta:
        db_table = "tblDefect"
    
    d_defectid = models.AutoField(primary_key=True)
    d_supplierinvoicenumber = models.ForeignKey(SupplierInvoice, on_delete=models.PROTECT)
    d_inventoryid = models.ForeignKey(MasterInventory,on_delete=models.PROTECT)
    d_employeeid = models.ForeignKey(
    	'accounts.Employee', on_delete=models.PROTECT)
    d_quantity = models.IntegerField(default=0)
    d_date = models.DateTimeField(auto_now_add=True)
    d_defectdesc = models.CharField(max_length=200, default="")

    def updatestock(self):
    	inventory = MasterInventory.objects.get(mi_inventoryid = str(self.d_inventoryid.mi_inventoryid))
    	inventory.updatestock(-self.d_quantity)