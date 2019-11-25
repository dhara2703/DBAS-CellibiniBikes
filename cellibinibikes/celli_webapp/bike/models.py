from django.db import models
# from masterInventory.models import MasterInventory
from django.apps import apps
#MasterInventoryModel = apps.get_model('masterInventory', 'MasterInventory')

# Create your models here.

class ModelType(models.Model):
	class Meta:
		db_table = "tblkModelType"

	modeltypeid = models.AutoField(primary_key=True)
	modeltypename = models.CharField(max_length=100)

	def __str__(self):
		return self.modeltypename

class BikeModel(models.Model):
	class Meta:
		db_table = "tblModel"
            
	modelid = models.AutoField(primary_key=True)
	modelname = models.CharField(max_length=100)
	modeltype = models.ForeignKey(ModelType, on_delete=models.SET("Discontinued"))#do we want it to cascade delete
	# thumb = models.ImageField(default='default.png', blank=True)

	def __str__(self):
		return self.modelname

class SubassemblyInventory(models.Model):
	class Meta:
		db_table = "jncSubassemblyInventory"

	subassemblyid = models.AutoField(primary_key=True)
	inventoryid = models.ForeignKey('masterInventory.MasterInventory', blank=True, null=True, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.inventoryid.partname


class Subassembly(models.Model):
	class Meta:
		db_table = "jncModelSubassembly"
		unique_together = (('modelid', 'subassemblyid'),)

	modelid = models.ForeignKey(BikeModel, on_delete=models.DO_NOTHING)
	subassemblyid = models.ForeignKey(
		SubassemblyInventory, on_delete=models.DO_NOTHING)
	quantity = models.IntegerField()

	def __str__(self):
		return self.inventoryid.partname


class PartInventory(models.Model):
	class Meta:
		db_table = "jncPartInventory"

	partid = models.AutoField(primary_key=True)
	inventoryid = models.ForeignKey(
		'masterInventory.MasterInventory', blank=True, null=True, on_delete=models.DO_NOTHING)

	def __str__(self):
		return str(self.inventoryid.partname)


class PartList(models.Model):
	class Meta:
		db_table = "tblPartList"
		unique_together = (('modelid', 'partid'),)

	modelid = models.ForeignKey(BikeModel, on_delete=models.DO_NOTHING)
	partid = models.ForeignKey('PartInventory', on_delete=models.DO_NOTHING)
	quantity = models.IntegerField()

	def __str__(self):
		return str(self.partid)

	def quantity(self):
		return str(self.quantity)


class SubassemblyPartsList(models.Model):
	class Meta:
		db_table = "tblSubassemblyPartsList"
		unique_together = (('subassemblyid', 'partid'),)

	subassemblyid = models.ForeignKey(
		SubassemblyInventory, on_delete=models.DO_NOTHING)
	partid = models.ForeignKey('PartInventory', on_delete=models.DO_NOTHING)
	quantity = models.IntegerField()

	def __str__(self):
		return str(self.partid)


class Bike(models.Model):
	class Meta:
		db_table = "tblBike"

	bikeid = models.AutoField(primary_key=True)
	modelid = models.ForeignKey(BikeModel, on_delete=models.DO_NOTHING)

	def __str__(self):
		return str(self.modelname)





  
