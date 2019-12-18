from django import forms
from django.contrib.auth.models import User
from . import models

class DocumentForm(forms.ModelForm):
    class Meta:
        model = models.Products
        fields = ['productImg', 'productTitle', 'productDescription', 'discountedPrice', 'marketPrice', 'deliveryCharges', 'productCategory']

class CategoryAdd(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['categoryName']