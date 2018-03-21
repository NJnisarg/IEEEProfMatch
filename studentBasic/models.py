from django.db import models

class studentBasic(models.Model):
	username = models.CharField(max_length=32,primary_key=True)
	firstName = models.CharField(max_length=100,blank=True)
	lastName = models.CharField(max_length=100,blank=True)
	state = models.CharField(max_length=100,blank=True)
	city = models.CharField(max_length=100,blank=True)
	gender = models.CharField(max_length=100,blank=True)
	age = models.PositiveIntegerField(blank=True)
	mobileNo = models.CharField(max_length=100,blank=True)


