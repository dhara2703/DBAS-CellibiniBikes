from django.contrib import admin
from .models import CustomerOrder
from .models import CustomerOrderLineItem
from .models import CustomerInvoice
from .models import CustomerInvoiceLineItem


# Register your models here.
admin.site.register(CustomerOrder)
admin.site.register(CustomerOrderLineItem)
admin.site.register(CustomerInvoice)
admin.site.register(CustomerInvoiceLineItem)
