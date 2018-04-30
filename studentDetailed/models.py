from django.db import models

class studentDetailed(models.Model):
    username = models.CharField(primary_key=True,max_length=32)
    cgpa = models.FloatField(blank=True,null=True)
    yearOfStudy = models.IntegerField(blank=True,null=True)
    branch = models.CharField(max_length=100,blank=True,null=True)
    institute = models.CharField(max_length=250,blank=True,null=True)
    workEx = models.IntegerField(blank=True,null=True)
    publications = models.TextField(blank=True,null=True)
    certificates = models.TextField(blank=True,null=True)
    personalProjects = models.TextField(blank=True,null=True)
    skillsInterest = models.TextField(blank=True,null=True)
    hobbies = models.TextField(blank=True,null=True)

