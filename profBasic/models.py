from django.db import models

class profBasic(models.Model):
    username = models.CharField(primary_key=True, max_length=32)
    firstName = models.CharField(max_length=100,blank=True)
    lastName = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=100,blank=True)
    gender = models.CharField(max_length=100,blank=True)
    age = models.PositiveIntegerField(blank=True)
    mobileNo = models.CharField(max_length=100,blank=True)
    institute = models.CharField(max_length=100,blank=True)
    department = models.CharField(max_length=100,blank=True)
    areas = models.TextField(blank=True)
    websiteLinks = models.TextField(blank=True)


