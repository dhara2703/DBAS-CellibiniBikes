from django import forms
from . import models


class CreateCustomerAccountForm(forms.ModelForm):
	class Meta:
		model = models.Customer
		fields = "__all_"
		#add restrictions for input later
