from django.urls import re_path, path
from . import views
app_name = 'bike'
urlpatterns = [
    re_path(r'^$', views.bike_list, name="bikelist"),
    re_path(r'^bikedetail/(?P<bikeid>[\w-]+)/$',
            views.bike_detail, name="bikedetail"),
    re_path(r'^bikemodelcreate/$', views.model_create, name="mcreate"),
    re_path(r'^bikemodels/$', views.bikemodels_list, name="bikemodelslist"),
    re_path(r'^bikemodels/(?P<modelid>[\w-]+)/$',
            views.bikemodel_detail, name="bikemodeldetail"),
]
