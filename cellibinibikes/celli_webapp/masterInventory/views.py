from django.shortcuts import render, redirect
from .models import MasterInventory
from . import forms

def inventory_list(request):
	inventories = MasterInventory.objects.all().order_by('mi_inventoryid')
	return render(request, 'masterInventory/inventory_list.html', {'inventories':inventories})

# def inventory_update(request):
#  	return 

# def inventory_order(request):
#  	return 

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

	return render(request, 'masterInventory/inventory_create.html', {'form': form})