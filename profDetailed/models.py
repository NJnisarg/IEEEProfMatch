from django.db import models


class profDetailed(models.Model):
    username = models.CharField(primary_key=True, max_length=32)
    areas = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    minWorkEx = models.PositiveIntegerField(blank=True, null=True)
    minYearOfStudy = models.PositiveIntegerField(blank=True, null=True)
    minCgpa = models.FloatField(blank=True, null=True)
    branch = models.TextField(blank=True, null=True)
    # selectedStudents = models.TextField(blank=True, null=True)


