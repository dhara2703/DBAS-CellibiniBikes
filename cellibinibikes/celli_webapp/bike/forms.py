from django import forms
from django.forms import modelformset_factory
from . import models


class BikeModelForm(forms.ModelForm):
	class Meta:
		model = models.BikeModel
		fields = ['modelname', 'modeltype']
		labels = {
		'modelname': 'Model Name',
		'modeltype': 'Model Type'
		}
		widgets = {
		'modelname': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Bike model'})
		}


PartsFormset = modelformset_factory(
    models.PartList,
    fields=('partid', 'partlist_quantity'),
    extra=2,
    widgets={
        'partlist_quantity': forms.NumberInput(
        	attrs={
        	'class': 'form-control',
        	'placeholder': 'Enter quantity here'}
        	),
        # 'partid': forms.ModelChoiceField(
        # 	queryset=models.PartInventory.objects.all())
    }
)