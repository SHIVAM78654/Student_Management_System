from django.db import models


# Create your models here.
class Stundent(models.Model):
    Fname = models.CharField(max_length=70)
    Lname = models.CharField(max_length=70)
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=100)
    branch = models.CharField(max_length=70)
    rollno = models.IntegerField()
    contactno = models.IntegerField()
    

    
