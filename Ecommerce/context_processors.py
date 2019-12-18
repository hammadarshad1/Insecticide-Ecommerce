from . import models
from Ecommerce import models as m
import mysql.connector
from django.http import request

def item_in_cart(request):
    product = m.Products.objects.all()
    conn = mysql.connector.connect(user='admin', host='localhost', port='3306', password='Gre@ter834', database='Ecommerce')
    cursor = conn.cursor()
    items = cursor.execute('''select sum((P.discountedPrice * C.productQuantity) + P.deliveryCharges) as SUM,
                              count(C.productId_id) as COUNT
                              from Ecommerce_cart C
                              JOIN Ecommerce_products as P
                              on C.productId_id = P.productId
                              where C.userId_id=%s''',[request.user.id])
    items = cursor.fetchall()
    categories = cursor.execute('''select categoryName, categoryId from Ecommerce_category''')
    categories = cursor.fetchall()
    slider = m.SliderImage.objects.all()
    if items[0][0] == None:
    	price = 0
    else:
        price = items[0][0]
    return {'Cart':items[0][1], 'Price':price, 'product':product[2], 'slider':slider, 'categories':categories}
