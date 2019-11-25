from django.shortcuts import render
from .models import ModelType, BikeModel


# Create your views here.

def model_list(request):
    models = BikeModel.objects.all().order_by('date')
    return render(request, 'bike/model_list.html', {'models':models})


def model_detail(request, modelid):
    model = BikeModel.objects.get(modelid=modelid)
    return render(request, 'bike/model_detail.html', {'model': model})
