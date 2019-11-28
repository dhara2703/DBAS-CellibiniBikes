from django import forms
from . import models


class CreateInventoryItem(forms.ModelForm):
	class Meta:
		model = models.MasterInventory
		fields = ['partname','numberofstocks','parlevel']
		#add restrictions for input later