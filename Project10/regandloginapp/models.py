from django.db import models

# Create your models here.
class Reg(models.Model):
    FirstName = models.CharField(max_length=10)
    LastName = models.CharField(max_length=10)
    UserName = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    cpassword = models.CharField(max_length=10)
    MobileNumber = models.IntegerField()
    Emailid = models.EmailField()