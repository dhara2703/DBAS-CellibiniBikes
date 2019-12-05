from django.urls import re_path, path
from . import views

app_name = 'customers'

urlpatterns = [
    re_path(r'^$', views.homepage, name='homepage'),
    re_path(r'^customer-order-list/$',
            views.customerorder_list, name='colist'),
    re_path(r'^customer-order-create/$', views.customerorder_create, name="ccreate"),


]

