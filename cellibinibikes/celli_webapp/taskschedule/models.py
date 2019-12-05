from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

    
class Task(models.Model):
    class Meta:
        db_table = "tblTask"

    t_taskid = models.AutoField(primary_key=True)
    t_bikeid = models.ForeignKey('bike.Bike', on_delete=models.PROTECT)
    t_customeroderid = models.ForeignKey('customers.CustomerOrder', on_delete=models.PROTECT)
    t_taskcreated = models.DateTimeField(auto_now_add=True)
    t_isactive = models.BooleanField(default=True)
    t_istaskcomplete = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.t_taskid)
    
    def bikemodel(self):
        return str(self.t_bikeid.b_modelid.bm_modelname)

    def firstame(self):
        return str(self.t_customeroderid.co_customerid.c_userid.first_name)
    
    def lastame(self):
        return str(self.t_customeroderid.co_customerid.c_userid.last_name)

    def companyname(self):
        return str(self.t_customeroderid.co_customerid.c_companyname)
        


class Schedule(models.Model):
    class Meta:
        db_table = "tblSchedule"

    s_scheduleid = models.AutoField(primary_key=True)
    s_scheduledate = models.DateTimeField()
    s_isactive = models.BooleanField(default=True)

    def __str__(self):
        return str(self.s_scheduleid)


class EmployeeSchedule(models.Model):
    class Meta:
        db_table = "jncSchedule"

    es_taskid = models.ManyToManyField(Task)
    es_scheduleid = models.ManyToManyField(Schedule)
    es_employeeid = models.ForeignKey(
        'accounts.Employee', on_delete=models.PROTECT)
    es_starttime = models.TimeField()
    es_endtime = models.TimeField()


    def taskid(self):
        return str(self.es_taskid)
    
    def scheduleid(self):
        return str(self.es_scheduleid)
    
    
