from django.db import models


class studentBasic(models.Model):
	username = models.CharField(max_length=32,primary_key=True)
	firstName = models.CharField(max_length=100,blank=True,null=True)
	lastName = models.CharField(max_length=100,blank=True,null=True)
	state = models.CharField(max_length=100,blank=True,null=True)
	city = models.CharField(max_length=100,blank=True,null=True)
	gender = models.CharField(max_length=100,blank=True,null=True)
	age = models.PositiveIntegerField(blank=True,null=True)
	mobileNo = models.CharField(max_length=100,blank=True,null=True)
	image_path = models.ImageField(upload_to='prof-match-images-data', blank=True, null=True)


