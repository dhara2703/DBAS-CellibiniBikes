from django.db import models

# Create your models here.
class CustomerOrder(models.Model):
    class Meta:
        db_table = "tblCustomerOrder"

    co_customeroderid = models.AutoField(primary_key=True)
    co_customerid = models.ForeignKey(
        'accounts.Customer', on_delete=models.PROTECT)
    co_paymentmethod = models.CharField(max_length=50)
    co_corderdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.co_customeroderid)
    
    def firstname(self):
        return str(self.co_customerid.c_userid.first_name)
    
    def lastname(self):
        return str(self.co_customerid.c_userid.last_name)
    
    def companyname(self):
        return str(self.co_customerid.c_companyname)

    def phonenumber(self):
        return str(self.co_customerid.c_phonenumber)
    
    def address(self):
        return ('%s %s %s' % (self.co_customerid.c_streetaddress1,
                              self.co_customerid.c_streetaddress2,
                              self.co_customerid.c_city,
                              self.co_customerid.c_province,
                              self.co_customerid.c_postalcode))
        
    def CustomerList(self):
        list = co_customerid.c_userid.objects.all()
        return list
    
    

class CustomerOrderLineItem(models.Model):
    class Meta:
        db_table = "jncCustomerOrderLineItem"

    coli_customeroderid = models.ForeignKey(
        CustomerOrder, on_delete=models.PROTECT)
    coli_bikeid = models.ForeignKey('bike.Bike', on_delete=models.PROTECT)
    coli_quantity = models.IntegerField()
    coli_isactive = models.BooleanField(default=True)

    def __str__(self):
        return str(self.coli_customeroderid)
    
    def modelname(self):
        return str(self.coli_bikeid.b_modelid.bm_modelname)


class CustomerInvoice(models.Model):
    class Meta:
        db_table = "tblCustomerInvoice"

    ci_invoiceid = models.AutoField(primary_key=True)
    ci_customeroderid = models.ForeignKey(
        CustomerOrder, on_delete=models.PROTECT)
    ci_date = models.DateTimeField(auto_now_add=True)
    ci_hst = models.DecimalField(decimal_places=2, max_digits=8)
    ci_subtotal = models.DecimalField(decimal_places=2, max_digits=14)
    ci_shippingfee = models.DecimalField(decimal_places=2, max_digits=6)
    ci_isactive = models.BooleanField(default=True)

    def __str__(self):
        return str(self.ci_customeroderid)


class CustomerInvoiceLineItem(models.Model):
    class Meta:
        db_table = "jncCustomerInvoieLineItem"

    cili_invoiceid = models.ForeignKey(
        CustomerInvoice, on_delete=models.PROTECT)
    cili_bikeid = models.ForeignKey('bike.Bike', on_delete=models.PROTECT)
    cili_quantityordered = models.IntegerField()
    cili_quantityshipped = models.IntegerField()
    cili_isactive = models.BooleanField(default=True)

    def __str__(self):
        return str(self.cili_invoiceid)
