from django.urls import re_path, path
from . import views

app_name = 'tasks'


urlpatterns = [
    re_path(r'^$', views.task_list, name='list'),
    re_path(r'schedulelist^$', views.schedule_list, name='slist'),
    re_path(r'^create/$', views.task_create, name='create'),
    re_path(r'^createschedule/$', views.schedule_create, name='screate'),    
]
