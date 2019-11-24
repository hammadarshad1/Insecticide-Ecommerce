from django.shortcuts import render, redirect
from . import models

# Create your views here.

def home(request):
    if request.method == "POST":
        searchText = request.POST.get("search")
        print(searchText)
        # searchProduct(request, searchProduct)
        # return redirect('Search')
    products = models.Products.objects.all()
    print(products)
    return render(request, 'Ecommerce/home.html', {'products': products})

def product_view(request, pk):
    product = models.Products.objects.get(productId=pk)
    print(product)
    return render(request, 'Ecommerce/product.html', {'product':product})

def about(request):
    return render(request, 'Ecommerce/about.html')

def searchProduct(request):
    return render(request, 'Ecommerce/search.html')