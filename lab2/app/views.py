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
from django.shortcuts import redirect
from .models import Products
from .models import Categories
from .models import Manufactories
from .models import Clients

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
            'products': Products.objects.all(),
        }
    )

def product(request, id):
    """Renders the products page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/product.html',
        {
            'title':'Product' ,
            'message':'Product ' + id + ' of Manto',
            'year':datetime.now().year,
            'product': Products.objects.get(pk = id),
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
            'users' : Db.getListUsers(),
            'year':datetime.now().year,
        }
    )

def getProduct(request, id):
    """Renders the products page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/getProduct.html',
        {
            'title':'Product to add in cart',
            'message':'All users Manto',
            'users' : ProductForm(),
            'year':datetime.now().year,
        }
    )

def addProduct(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ProductForm(request.POST)
            if form.is_valid():
                name = form.data['name']
                title = form.data['title']
                categoryId = form.data['category']
                manufactoryId = form.data['manufactory']
                Db.addProduct(name, title, categoryId, manufactoryId)
                return redirect('/products')
        else:
            form = ProductForm()
        return render(
            request,
            'app/addProduct.html',
            {
                'title':'Add product',
                'message':'All users Manto',
                'year':datetime.now().year,
                'form' : form,
                'product' : "",
                'manufactories' : Db.getListManufactories,
                'categories' : Db.getListCategories,
            }
        )
    else:
      return redirect('/login') 

def editProduct(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ProductForm(request.POST)
            if form.is_valid():                
                product = Products.objects.get(pk = id)
                product.name = form.data['name']
                product.title = form.cleaned_data['title']
                product.manufactory = Manufactories.objects.get(pk = form.data['manufactory'])
                product.category = Categories.objects.get(pk = form.data['category'])
                product.save()
                return redirect('/product/' + id)
        else:
            product = Products.objects.get(pk = id)
            form = ProductForm(initial={
                'name': product.name, 
                'title' : product.title, 
                'manufactory' : product.manufactory.id,
                'category' : product.category.id,
            })
        return render(
            request,
            'app/addProduct.html',
            {
                'title':'Edit product',
                'message':'All users Manto',
                'year':datetime.now().year,
                'form' : form,
            }
        )
    else:
      return redirect('/login') 

def deleteProduct(request, id):
    if request.user.is_authenticated:
        product = Db.getProduct(id)
        return render(
            request,
            'app/removeProduct.html',
            {
                'title':'Remove product',
                'message':'All users Manto',
                'year':datetime.now().year,
                'msg' : Db.deleteProduct(id),
                'product' : product,
            }
        )
    else:
      return redirect('/login') 
