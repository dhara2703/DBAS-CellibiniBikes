from django.conf.urls import url
from . import views

app_name = "masterInventory"

urlpatterns = [
	url(r'^$', views.inventory_list, name="inventorylist"),  # view all the inventory
	url(r'^pdf/inventories', views.Pdfinventory, name="inventorylistpdf"),


	url(r'^inventoryorder/create$', views.inventoryorder_create, name="inventoryorder"),
	url(r'^inventoryorder/list$', views.inventoryorder_list, name="inventoryorderlist"),
	url(r'^inventoryorder/detail/(?P<orderid>[\w-]+)$', views.inventoryorder_detail, name="inventoryorderdetail"),
	url(r'^inventoryorder/renderpdf/(?P<orderid>[\w-]+)$', views.pdforder, name="inventoryorderpdf" ),

	url(r'^inventoryorder/approve/(?P<orderid>[\w-]+)$',views.inventoryinvoice_create, name="inventoryorderapprove"),
	#invoice routes
	url(r'^inventoryinvoice/list$', views.inventoryinvoice_list,name="inventoryinvoicelist"),
	url(r'^inventoryinvoice/detail/(?P<invoiceid>[\w-]+)$',views.inventoryinvoice_detail, name="inventoryinvoicedetail"),
	url(r'^inventoryinvoice/renderpdf/(?P<invoiceid>[\w-]+)$', views.pdfinvoice, name="inventoryinvoicepdf" ),
	#supplier routes
	url(r'^itemcreate/$', views.inventory_item_create, name="inventoryadd"),
	url(r'^supplierlist/$', views.supplier_list, name="supplierlist"),

	#defects routes
	url(r'^defects/$', views.defects_list, name="defectslist"),
	url(r'^defects/report/(?P<invoiceid>[\w-]+)$', views.defect_create, name="defectcreate"),
	url(r'^defects/detail/(?P<defectinvoiceid>[\w-]+)/$', views.defect_detail, name="defectdetail"),
	# url(r'^defects/reportdefect$', views.create_defect, name="createdefect"),


]
