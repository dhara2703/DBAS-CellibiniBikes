from django.urls import re_path, path
from . import views
from django.contrib import admin

app_name = 'accounts'

urlpatterns = [
    # re_path(r'^signup/$', views.signup_view, name='signup'),
    re_path(r'^login/$', views.login_view, name="login"),
    re_path(r'^logout/$', views.logout_view, name='logout'),
    re_path(r'^employeecreate/$', views.employee_create, name="ecreate"),
    re_path(r'^customercreate/$', views.customer_create, name="ccreate"),
    re_path(r'^customers/$', views.customer_list, name='clist'),
    re_path(r'^employees/$', views.employee_list, name='elist'),
]
