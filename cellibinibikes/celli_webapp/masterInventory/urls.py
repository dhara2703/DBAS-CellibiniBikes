from django.conf.urls import url
from . import views

app_name = "masterInventory"

urlpatterns = [
	url(r'^$', views.inventory_list, name="inventorylist"), #view all the inventory
	#url(r'^update/$', views.inventory_update, name="inventoryupdate"), #update the inventory
	url(r'^itemcreate/$', views.inventory_item_create, name="inventoryadd"),

]