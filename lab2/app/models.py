"""
Definition of models.
"""

from django.db import models
from django.forms import ModelForm

# Create your models here.

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

class Clients(models.Model):
    fname = models.CharField(max_length = 30)
    lname = models.CharField(max_length = 30)
    date = models.DateField()
    products = models.ForeignKey(Products)

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'title', 'category', 'manufactory']

