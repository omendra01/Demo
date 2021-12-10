from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

# Create your models here.
class StudentRecord(models.Model):
    student_name = models.CharField(max_length=255,blank=True,null=True)
    father_name = models.CharField(max_length=255,blank=True,null=True)
    dob = models.CharField(max_length=255,blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    city = models.CharField(max_length=255,blank=True,null=True)
    state = models.CharField(max_length=255,blank=True,null=True)
    pin = models.CharField(max_length=255,blank=True,null=True)
    phone_no = models.CharField(max_length=255,unique=True)
    email = models.CharField(max_length=255,unique=True)
    class_opted = models.CharField(max_length=255,blank=True,null=True)
    marks = models.CharField(max_length=255,blank=True,null=True)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name
