"""
Definition of forms.
"""
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Categories
from .models import Manufactories

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class ProductForm(forms.Form):
    name = forms.CharField(max_length=30, required = True,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':'Name'}))
    title = forms.CharField(max_length=30,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':'Title'}))
    category = forms.ChoiceField(label="Categories", choices=([(category.id, category.name) for category in Categories.objects.all()]), required = True,
                                       widget=forms.Select(attrs={'class':'form-control'}))
    manufactory = forms.ChoiceField(label="Manufactories", choices=([(manufactory.id, manufactory.name) for manufactory in Manufactories.objects.all()]), required = True,
                                       widget=forms.Select(attrs={'class':'form-control'}))

