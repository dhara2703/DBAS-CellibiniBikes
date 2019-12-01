from django import forms
from django.forms import modelformset_factory
from . import models


class BikeModelForm(forms.ModelForm):
	class Meta:
		model = models.BikeModel
		fields = ['bm_modelname', 'bm_modeltype']
		labels = {
                    'bm_modelname': 'Model Name',
                    'bm_modeltype': 'Model Type'
		}
		widgets = {
                    'bm_modelname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bike model'})
		}


PartsFormset = modelformset_factory(
    models.PartList,
    fields=('pl_partid', 'pl_quantity'),
    extra=2,
    widgets={
        'pl_quantity': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter quantity here'}
        ),
        # 'partid': forms.ModelChoiceField(
        # 	queryset=models.PartInventory.objects.all())
    }
)
