from django.contrib import admin
from .models import MasterInventory
from .models import Supplier
from .models import SupplierOrder
from .models import SupplierOrderLineItem
#from .models import SupplierInvoice
# from .models import SupplierInvoiceLineItem
#from .models import Defect


# Register your models here.
admin.site.register(MasterInventory)
admin.site.register(Supplier)
admin.site.register(SupplierOrder)
#admin.site.register(SupplierOrderLineItem)
# admin.site.register(SupplierInvoice)
#admin.site.register(Defect)
