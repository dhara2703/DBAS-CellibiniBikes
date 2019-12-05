from django.contrib import admin
from .models import ModelType
from .models import BikeModel
from .models import SubassemblyInventory
from .models import Subassembly
from .models import PartInventory
from .models import PartList
from .models import SubassemblyPartsList
from .models import BikeStatus
from .models import Bike

# Register your models here.
admin.site.register(ModelType)
admin.site.register(BikeModel)
admin.site.register(Subassembly)
admin.site.register(SubassemblyInventory)
admin.site.register(PartInventory)
admin.site.register(PartList)
admin.site.register(SubassemblyPartsList)
admin.site.register(Bike)
admin.site.register(BikeStatus)
