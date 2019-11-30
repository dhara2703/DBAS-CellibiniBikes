from django.db import models
from masterInventory.models import MasterInventory
from django.apps import apps


class ModelType(models.Model):
	class Meta:
		db_table = "tblkModelType"

	mt_modeltypeid = models.AutoField(primary_key=True)
	mt_modeltypename = models.CharField(max_length=100)
	mt_isactive = models.BooleanField(default=True)
​
	def __str__(self):
		return self.mt_modeltypename


class BikeModel(models.Model):
	class Meta:
		db_table = "tblModel"
            
	bm_modelid = models.AutoField(primary_key=True)
	bm_modelname = models.CharField(max_length=100)
	bm_modeltype = models.ForeignKey(ModelType, on_delete=models.SET("Discontinued"))#do we want it to cascade delete
	bm_thumb = models.ImageField(default='default.png', blank=True)
	bm_isactive = models.BooleanField(default=True)

	def __str__(self):
		return self.modelname

class SubassemblyInventory(models.Model):
	class Meta:
		db_table = "jncSubassemblyInventory"
​
	si_subassemblyid = models.AutoField(primary_key=True)
	si_inventoryid = models.ForeignKey('masterInventory.MasterInventory', blank=True, null=True, on_delete=models.DO_NOTHING)
​
	def __str__(self):
		return self.si_inventoryid.mi_partname

class Subassembly(models.Model):
	class Meta:
		db_table = "jncModelSubassembly"
		unique_together = (('s_modelid', 's_subassemblyid'),)
​
	s_modelid = models.ForeignKey(BikeModel, on_delete=models.DO_NOTHING)
	s_subassemblyid = models.ForeignKey(SubassemblyInventory, on_delete=models.DO_NOTHING)
	s_quantity = models.IntegerField()
	s_isactive = models.BooleanField(default=True)
​
	def __str__(self):
		return self.s_subassemblyid.si_inventoryid.mi_partname

class PartInventory(models.Model):
	class Meta:
		db_table = "jncPartInventory"
​
	pi_partid = models.AutoField(primary_key=True)
	pi_inventoryid = models.ForeignKey('masterInventory.MasterInventory', blank=True, null=True, on_delete=models.DO_NOTHING)
	pi_isactive = models.BooleanField(default=True)
​
	def __str__(self):
		return str(self.pi_inventoryid.mi_partname)

class PartList(models.Model):
	class Meta:
		db_table = "tblPartList"
		unique_together = ('pl_modelid', 'pl_partid')
​
	pl_modelid = models.ForeignKey(BikeModel, on_delete=models.DO_NOTHING)
	pl_partid = models.ForeignKey('PartInventory', on_delete=models.DO_NOTHING)
	pl_quantity = models.IntegerField(default=0)
 
	def __str__(self):
    		return str(self.partid)
	def quantity(self):
		return str(self.quantity)

class SubassemblyPartsList(models.Model):
	class Meta:
		db_table = "tblSubassemblyPartsList"
		unique_together = ('spl_subassemblyid', 'spl_partid')
​
	spl_subassemblyid = models.ForeignKey(SubassemblyInventory, on_delete=models.DO_NOTHING)
	spl_partid = models.ForeignKey('PartInventory', on_delete=models.DO_NOTHING)
	spl_quantity = models.IntegerField()
	spl_isactive = models.BooleanField(default=True)
​
	def __str__(self):
		return str(self.spl_partid)


class Bike(models.Model):
	class Meta:
		db_table = "tblBike"
​
	b_bikeid = models.AutoField(primary_key=True)
	b_modelid = models.ForeignKey(BikeModel, on_delete=models.DO_NOTHING)
​
	def __str__(self):
		return str(self.b_modelid.bm_modelname)




  
