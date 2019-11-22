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

    # this function is created to display a snippet on screen for the model
    # to call this function in views : <td>{{ task.modeldescription }}</td> TO <td>{{ task.snippet }}</td>
    # Ninja video 11 : https://www.youtube.com/watch?v=ERCt6HUcaFw&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc&index=11 
    def snippet(self):
        return self.body[:50] + ' ...'  # Displays 50 characters

