from django.shortcuts import render
from .models import ModelType, BikeModel
from . import forms


# Create your views here.

def model_list(request):
    models = BikeModel.objects.all().order_by('date')
    return render(request, 'bike/model_list.html', {'models':models})


def model_detail(request, modelid):
    model = BikeModel.objects.get(modelid=modelid)
    return render(request, 'bike/model_detail.html', {'model': model})

def model_create(request):
	if request.method =='POST':
		bikemodelform = forms.BikeModelForm(request.POST)
		partlistformset = forms.PartsFormset(request.POST)
		if bikemodelform.is_valid() and partlistformset.is_valid():
			#save form to db
			bikeinstance = bikemodelform.save()
			for form in partlistformset:
				
				partlist = form.save(commit=False)
				partlist.partid = form['partid']
				partlist.quantity = form['quantity']

			return redirect('bike:list')
	else:
		bikemodelform = forms.BikeModelForm()
		partlistformset = forms.PartsFormset()
	return render(request, 'bike/model_create.html',{'bikemodelform':bikemodelform, 'partlistformset':partlistformset})