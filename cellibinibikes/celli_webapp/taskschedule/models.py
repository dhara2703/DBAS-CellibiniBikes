from django.db import models

# Create your models here.


class Task(models.Model):
    taskid = models.IntegerField(primary_key=True)
    employeeid = models.IntegerField()
    bikeid = models.IntegerField()
    custoemrorderid = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.employeeid)



