from django import forms
from . import models
​
​
class CreateInventoryItem(forms.ModelForm):
	class Meta:
		model = models.MasterInventory
		fields = ['mi_partname', 'mi_numberofstocks', 'mi_parlevel']
		#add restrictions for input later