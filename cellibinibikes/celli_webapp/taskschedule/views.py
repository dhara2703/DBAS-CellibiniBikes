from django.shortcuts import render
from .models import Task
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def task_list(request):
    tasks = Task.objects.all().order_by('date')
    return render(request, 'taskschedule/task_list.html', {'tasks': tasks})


# Ninja video 11 : https://www.youtube.com/watch?v=c2hbT0uIcOQ&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc&index=14
def task_detail(request, bikeid):
    #  return HttpResponse(bikeid)
    task = Task.objects.get(bikeid=bikeid)
    return render(request, 'taskschedule/task_detail.html', {'task': task})


@login_required(login_url="/accounts/login/")
def task_create(request):
    return render(request, 'taskschedule/task_create.html')

# def model_list(request):
#     models = Model.objects.all().order_by('date')
#     return render(request, 'taskschedule/model_list.html', {'models':models})


# def model_detail(request, modelid):
#     model = Model.objects.get(modelid=modelid)
#     return render(request, 'taskschedule/model_detail.html', {'model': model})
