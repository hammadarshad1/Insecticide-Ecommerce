from django.shortcuts import render, redirect
from . import models
from django.views.generic import ListView
import mysql.connector
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required


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

def addtocart(request, pk):
    product = models.Products.objects.get(productId = pk)
    if models.Cart.objects.filter(Q(productId=product) & Q(userId=request.user)):
        messages.warning(request, 'This product is already in Your Cart')
        return redirect('Cart')
    else:    
        cart = models.Cart(productId=product, userId=request.user, productQuantity=1)
        cart.save()
        messages.success(request, 'Product Added to Cart')
        return redirect('Home')

@login_required
def product_cart(request):
    products = models.Cart.objects.filter(userId = request.user)
    return render(request,'Ecommerce/cart.html', {'products':products})

def delete_cart_item(request, pk):
    c = models.Cart.objects.filter(productId = pk, userId=request.user).delete()
    return redirect('Cart')