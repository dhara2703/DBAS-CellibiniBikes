from django.urls import re_path, path
from . import views

app_name = 'tasks'


urlpatterns = [
    re_path(r'^$', views.task_list, name='list'),
    re_path(r'^(?P<bikeid>[\w-]+)/$', views.task_detail, name="detail"),
    # re_path(r'^models', views.model_list, name="list"),
    # re_path(r'^models/^(?P<modelid>[\w-]+)/$', views.model_detail, name="mdetail"),

    # path('', views.task_list),
    # path('<slug>/', views.task_detail)
]
