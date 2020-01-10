from django.urls import re_path, path
from . import views

app_name = 'customers'

urlpatterns = [
    re_path(r'^$', views.customerorderlist, name='colist'),
    re_path(r'^customerorderlist/$',
            views.customerorderlist, name='colist'),
    re_path(r'^customerordercreate/$',
            views.customerordercreate, name="cocreate"),
    re_path(r'^(?P<co_customeroderid_id>[\w-]+)$',
            views.customeroderinlinecreate, name="coinlinecreate"),
    

]

