from django.shortcuts import render, redirect
from .models import *
from . import forms
# Create your views here.


def bike_list(request):
	bikes = Bike.objects.all()
	return render(request, 'bike/bike_list.html', {'bikes': bikes})


def bike_detail(request, bikeid):
	bike = Bike.objects.get(b_bikeid=bikeid)
	bikepartslists = PartList.objects.filter(pl_modelid=bike.b_modelid)
	bikesubassemblys = Subassembly.objects.filter(s_modelid=bike.b_modelid)
	return render(request, 'bike/bike_detail.html', {'bike': bike, 'bikepartslists': bikepartslists, 'bikesubassemblys': bikesubassemblys})


def model_create(request):
	if request.method == 'POST':
		bikemodelform = forms.BikeModelForm(request.POST)
		partlistformset = forms.PartsFormset(request.POST)
		if bikemodelform.is_valid() and partlistformset.is_valid():
			#save form to db
			bikeinstance = bikemodelform.save()
			for form in partlistformset:
				partlist = form.save(commit=False)
				partlist.pl_partid = form['pl_partid']
				partlist.pl_quantity = form['pl_quantity']
			return redirect('bike:list')
	else:
		bikemodelform = forms.BikeModelForm()
		partlistformset = forms.PartsFormset()
	return render(request, 'bike/model_create.html', {'bikemodelform': bikemodelform, 'partlistformset': partlistformset})


def bikemodels_list(request):
	BikeModels = BikeModel.objects.all()
	return render(request, 'model/model_list.html', {'BikeModels': BikeModels})


def bikemodel_detail(request, modelid):
	bikeModel = BikeModel.objects.get(bm_modelid=modelid)
	bikepartslists = PartList.objects.filter(pl_modelid=bikeModel.bm_modelid)
	bikesubassemblys = Subassembly.objects.filter(s_modelid=bikeModel.bm_modelid)
	return render(request, 'model/model_detail.html', {'bikeModel': bikeModel, 'bikepartslists': bikepartslists, 'bikesubassemblys': bikesubassemblys})
