from django.contrib import admin
from django.urls import include, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

# Change admin site title
admin.site.site_header = "Cellibini Bikes Company WebApp Login"
admin.site.site_title = "Cellibini Bikes Company"

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path(r'^admin/', admin.site.urls),
    
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^taskschedule/', include('taskschedule.urls')),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^customers/', include('customers.urls')),
    re_path(r'^bike/', include('bike.urls')),
    re_path(r'^masterinventory/', include('masterInventory.urls')),
    re_path(r'^about/$', views.about),
    re_path(r'^$', views.homepage),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
