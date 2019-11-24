from django.shortcuts import render, redirect
from . import models
from django.views.generic import ListView
import mysql.connector

# Create your views here.

# def home(request):
#     if request.method == "POST":
#         searchText = request.POST.get("search")
#         print(searchText)
#         # searchProduct(request, searchProduct)
#         # return redirect('Search')
#     products = models.Products.objects.all()
#     print(products)
#     return render(request, 'Ecommerce/home.html', {'products': products})

conn = mysql.connector.connect(user='admin', host='localhost', port='3306', password='Gre@ter834', database="Ecommerce")

class ProductsListView(ListView):
    model = models.Products
    template_name = 'Ecommerce/home.html'
    paginate_by = 20

def product_view(request, pk):
    product = models.Products.objects.get(productId=pk)
    print(product)
    return render(request, 'Ecommerce/product.html', {'product':product})

def about(request):
    return render(request, 'Ecommerce/about.html')

def searchProduct(request):
    if request.method == "POST":
        Search = request.POST.get('search')
        print(Search)
        # string = input('Enter Search: ')
        a = Search.split(' ')
        query="""select * from Ecommerce_products where productTitle LIKE """

        for li in a:
            if a[-1] == li:
                query += "'%{}%' OR '%{}' OR '{}%' ".format(li, li, li)
                # a.pop(a.index(li))
            else:
                query += "'%{}%' OR '{}%' OR '%{}' AND ".format(li, li, li)
                # a.pop(a.index(li))
        print(query)
        try:
            cursor = conn.cursor()
            query = cursor.execute(query)
            query = cursor.fetchall()
        except:
            return redirect('Error404')
        if not query:
            return redirect('Pr-Not-Found')
            
        print(query)
    return render(request, 'Ecommerce/search.html', {'search':query})

def err404(request):
    return render(request, 'Ecommerce/404.html')

def errNotFound(request):
    return render(request, 'Ecommerce/pr-not-found.html')