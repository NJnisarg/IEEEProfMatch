from django.db import models

class studentDetailed(models.Model):
    username = models.CharField(primary_key=True,max_length=32)
    cgpa = models.IntegerField(blank=True)
    yearOfStudy = models.IntegerField(blank=True)
    branch = models.CharField(max_length=100,blank=True)
    institute = models.CharField(max_length=250,blank=True)
    workEx = models.TextField(blank=True)
    publications = models.TextField(blank=True)
    certificates = models.TextField(blank=True)
    personalProjects = models.TextField(blank=True)
    skillsInterest = models.TextField(blank=True)
    hobbies = models.TextField(blank=True)

