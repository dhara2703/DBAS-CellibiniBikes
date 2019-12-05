from django.contrib import admin
from .models import Task
from .models import Schedule

# Register your models here.

admin.site.register(Task)
admin.site.register(Schedule)

