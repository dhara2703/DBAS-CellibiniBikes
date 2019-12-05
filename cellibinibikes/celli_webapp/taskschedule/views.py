from django.shortcuts import render
from .models import Task, Schedule, EmployeeSchedule
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/accounts/login/")
def task_create(request, t_taskid):
    task = Task.objects.get(t_taskid=t_taskid)
    return render(request, 'taskschedule/task_create.html', {'task': task})


@login_required(login_url="/accounts/login/")
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'taskschedule/task_list.html', {'tasks': tasks})


# # Ninja video 11 : https://www.youtube.com/watch?v=c2hbT0uIcOQ&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc&index=14
# @login_required(login_url="/accounts/login/")
# def task_detail(request, t_taskid):
#     task = Task.objects.get(t_taskid=t_taskid)
#     return render(request, 'taskschedule/task_detail.html', {'task': task})


@login_required(login_url="/accounts/login/")
def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'taskschedule/schedule_list.html', {'schedules': schedules})


@login_required(login_url="/accounts/login/")
def schedule_create(request, s_scheduleid):
    schedule = Schedule.objects.get(s_scheduleid=s_scheduleid)
    return render(request, 'taskschedule/schedule_create.html', {'schedule': schedule})
