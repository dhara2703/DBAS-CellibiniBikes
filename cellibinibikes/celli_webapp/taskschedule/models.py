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

#     def customerName(self):
#         return str(self.custoemrorderid.name)


class Schedule(models.Model):
    class Meta:
        db_table = "tblSchedule"

    s_scheduleid = models.AutoField(primary_key=True)
    s_taskid = models.ForeignKey(Task, on_delete=models.PROTECT)
    s_employeeid = models.ForeignKey(
        'accounts.Employee', on_delete=models.PROTECT)
    s_starttime = models.TimeField()
    s_endtime = models.TimeField()
    s_scheduledate = models.DateTimeField()
    s_isactive = models.BooleanField(default=True)

    def __str__(self):
        return str(self.s_scheduleid)




