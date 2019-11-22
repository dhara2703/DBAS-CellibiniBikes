from django.urls import re_path, path
from . import views

app_name = 'customers'

urlpatterns = [
    re_path(r'^$', views.homepage, name='homepage'),
]
