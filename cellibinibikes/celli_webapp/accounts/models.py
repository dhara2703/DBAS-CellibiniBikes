from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.


class Employee(models.Model):
    class Meta:
        db_table = "tblEmployee"

    e_userid = models.OneToOneField(User, primary_key=True, on_delete=models.PROTECT)
    e_streetaddress1 = models.CharField(blank=False, max_length=100)
    e_streetaddress2 = models.CharField(blank=True, max_length=100)
    e_city = models.CharField(blank=False, max_length=100)
    e_province = models.CharField(blank=False, max_length=100)
    e_postalcode = models.CharField(blank=False, max_length=6)
    e_country = models.CharField(blank=False, default='CA', max_length=100)
    e_phonenumber = models.CharField(blank=False, max_length=15)
    e_salary = models.DecimalField(decimal_places=2, max_digits=10)
    e_startdate = models.DateField(null=False)
    # e_stoptdate = models.DateField(blank=True, default='', null=True)
    e_sinnumber = models.CharField(max_length=9)
    e_isapprentice = models.BooleanField(default=False)

    # def get_queryset(self):
    #     return super(Employee, self).get_queryset().filter(isapprentice = True)

    def __str__(self):
        return str(self.e_userid.username)
    
    def firstname(self):
        return str(self.e_userid.first_name)

    def lastname(self):
        return str(self.e_userid.last_name)
    
    def formatted_salary(self):
        return '%.2f CAD' % self.e_salary
    
        

class Customer(models.Model):
    class Meta:
        db_table = "tblCustomer"

    c_customerid = models.AutoField(primary_key=True)
    c_userid = models.OneToOneField(User, on_delete=models.PROTECT)
    c_streetaddress1 = models.CharField(blank=False, max_length=100)
    c_streetaddress2 = models.CharField(blank=True, max_length=100)
    c_city = models.CharField(blank=False, max_length=100)
    c_province = models.CharField(blank=False, max_length=100)
    c_postalcode = models.CharField(blank=False, max_length=6)
    c_country = models.CharField(blank=False, default='CA', max_length=100)
    c_phonenumber = models.CharField(blank=False, max_length=15)
    c_dateregistered = models.DateTimeField(auto_now_add=True)
    c_issubscribed = models.BooleanField(default=True)
    c_companyname = models.CharField(blank=True, max_length=150)
    c_isactive = models.BooleanField(default=True)

    def __str__(self):
        return str(self.c_customerid)
    
    def firstname(self):
        return str(self.c_userid.first_name)
    
    def lastname(self):
        return str(self.c_userid.last_name)
    
    def email(self):
        return str.lower(self.c_userid.email)
    
    
    
    
