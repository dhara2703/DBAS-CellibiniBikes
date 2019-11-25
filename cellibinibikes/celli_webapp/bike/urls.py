from django.urls import re_path, path
from . import views

app_name = 'bike'


urlpatterns = [
    re_path(r'^', views.model_list, name="list"),
    re_path(r'^(?P<modelid>[\w-]+)/$', views.model_detail, name="mdetail"),
]
