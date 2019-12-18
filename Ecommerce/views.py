from django.shortcuts import render, redirect
from . import models
from django.views.generic import ListView
import mysql.connector
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from .forms import DocumentForm, CategoryAdd
import json

conn = mysql.connector.connect(user='admin', host='localhost', port='3306', password='Gre@ter834', database="Ecommerce")

class ProductsListView(ListView):
    model = models.Products
    template_name = 'Ecommerce/home.html'
    paginate_by = 20
    context = {'slider':True}
    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs)                     
        new_context_entry = models.SliderImage.objects.all()
        context["slider"] = new_context_entry
        context['sliderAllow'] = 1
        return context

def product_view(request, pk):
    product = models.Products.objects.get(productId=pk)
    comment = models.Comments.objects.filter(Q(productId = product)).all()
    relatedProduct = models.Products.objects.filter(Q(productCategory = product.productCategory) & ~Q(productId = product.productId))
    print(product)
    if request.method == 'POST':
        text = request.POST.get('text')
        c = models.Comments(commentText=text, productId=product, userId=request.user)
        c.save()
        print('saved')
    return render(request, 'Ecommerce/product.html', {'product':product, 'relatedProducts': relatedProduct[0:5], 'comment':comment})

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
    if request.method == 'POST':
        if request.POST.get('samp') == 'samp':
            items = json.loads(request.POST.get('items'))
            print(items)
            for item in items:
                print(item)
                itemName = item['productName']
                item_add = models.Order(productId = models.Products.objects.get(productTitle=itemName), orderQuantity=1, userId=request.user)
                item_add.save()
            models.Cart.objects.filter(userId = request.user).all().delete()
            messages.success(request, 'successfully orderd! you will be respond in 24 hours!')
            return JsonResponse({'succes':'success'})
    return render(request,'Ecommerce/cart.html', {'products':products})

def delete_cart_item(request, pk):
    c = models.Cart.objects.filter(productId = pk, userId=request.user).delete()
    return redirect('Cart')

@login_required
def new_product(request):
    category = models.Category.objects.all()
    form = DocumentForm(request.POST, request.FILES)

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')
        else:
            form = DocumentForm()
        category = models.Category.objects.get(categoryId = category)
        p = models.Products.objects.last()
        p.productCategory = category
        p.userId = request.user
        p.save()
        messages.success(request, 'Product Added To cart')
        return redirect('Home')
    return render(request, 'Ecommerce/add-product.html', {'category':category, 'form':form})

@login_required
def profile_products(request):
    cursor = conn.cursor()
    cursor.execute('''select * from Ecommerce_products where userId_id=%s''',[request.user.id])
    products = cursor.fetchall()
    return render(request, 'Ecommerce/profile-products.html',{'products',products})

@login_required
def add_category(request):
    form = CategoryAdd(request.POST)
    if request.method == "POST":
        form  = CategoryAdd(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Added Category!')
            return redirect('Home')
    return render(request, 'Ecommerce/category.html', {'form':form})