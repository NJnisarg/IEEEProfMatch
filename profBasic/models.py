from django.db import models

class profBasic(models.Model):
    username = models.CharField(primary_key=True, max_length=32)
    firstName = models.CharField(max_length=100,blank=True,null=True)
    lastName = models.CharField(max_length=100,blank=True,null=True)
    state = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    gender = models.CharField(max_length=100,blank=True,null=True)
    age = models.PositiveIntegerField(blank=True,null=True)
    mobileNo = models.CharField(max_length=100,blank=True,null=True)
    institute = models.CharField(max_length=100,blank=True,null=True)
    department = models.CharField(max_length=100,blank=True,null=True)
    areas = models.TextField(blank=True,null=True)
    websiteLinks = models.TextField(blank=True,null=True)


