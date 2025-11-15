from django.db import models

class Animals(models.Model):
    name=models.CharField(max_length=40)
    species=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    age=models.FloatField()
    habitat=models.CharField(max_length=20)
    
class caretaker(models.Model):
    name=models.CharField(max_length=40)
    gender=models.CharField(max_length=10)
    age=models.FloatField()
    experience=models.FloatField()
    phone_number=models.IntegerField()
    
class donated_by(models.Model):
    name=models.CharField(max_length=40)
    Type=models.CharField(max_length=20)
    address=models.CharField(max_length=40)
    phone_number=models.IntegerField()
    reason_for_donation=models.CharField(max_length=40)    

    
# Create your models here.

# Create your models here.
