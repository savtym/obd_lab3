"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import mysql.connector
from .forms import ProductForm
from .db import Db

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Manto',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Contacts of Manto',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Manto is shop for you',
            'year':datetime.now().year,
        }
    )

def products(request):
    """Renders the products page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/products.html',
        {
            'title':'Products',
            'message':'All products Manto',
            'year':datetime.now().year,
            'products':Db.getListProducts,
        }
    )

def product(request, id = 0):
    """Renders the products page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/product.html',
        {
            'title':'Product',
            'message':'Product ' + id + ' of Manto',
            'year':datetime.now().year,
            'product':Db.getProduct(id),
        }
    )

def users(request):
    """Renders the products page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/users.html',
        {
            'title':'Users',
            'message':'All users Manto',
            'users' : db.getListUsers(),
            'year':datetime.now().year,
        }
    )

def addProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.data['name']
            title = form.data['title']
            categoryId = form.data['category']
            manufactoryId = form.data['manufactory']
            Db.addProduct(name, title, categoryId, manufactoryId)
            #return redirect('app.views.products')
    else:
        form = ProductForm()
    return render(
        request,
        'app/addProduct.html',
        {
            'title':'Users',
            'message':'All users Manto',
            'year':datetime.now().year,
            'form' : form,
            'manufactories' : Db.getListManufactories,
            'categories' : Db.getListCategories,
        }
    )