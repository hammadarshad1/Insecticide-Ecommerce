from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    products = models.Products.objects.all()
    return render(request, 'Ecommerce/home.html', {'products': products})