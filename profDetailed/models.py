from django.db import models

class profDetailed(models.Model):
    username = models.CharField(primary_key=True, max_length=32)
    areas = models.TextField(blank=True)
    keywords = models.TextField(blank=True)
    minWorkEx = models.PositiveIntegerField(blank=True)
    minYearOfStudy = models.PositiveIntegerField(blank=True)
    minCgpa = models.PositiveIntegerField(blank=True)
    branch = models.TextField(blank=True)


