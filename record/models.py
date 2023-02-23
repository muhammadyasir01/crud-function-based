from django.db import models

class DataBase (models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    section = models.CharField(max_length=50)