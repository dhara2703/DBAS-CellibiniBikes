from django.db import models

# Create your models here.
class MasterInventory(models.Model):
	class Meta:
		db_table = "tblMasterInventory"
		
	inventoryid = models.AutoField(primary_key=True)
	#partid = 
	partname = models.CharField(max_length=100)
	numberofstocks = models.IntegerField()
	parlevel = models.IntegerField()

	

	def __str__(self):
		return str(self.partname)