"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Clients(models.Model):
    fname = models.CharField(max_length = 30)
    lname = models.CharField(max_length = 30)
    date = models.DateField()

class Categories(models.Model):
    name = models.CharField(max_length = 30)
    title = models.CharField(max_length = 30)

class Manufactories(models.Model):
    name = models.CharField(max_length = 30)
    region = models.CharField(max_length = 30)

class Products(models.Model):
    name = models.CharField(max_length = 30)
    title = models.CharField(max_length = 30)
    category = models.ForeignKey(Categories)
    manufactory = models.ForeignKey(Manufactories)