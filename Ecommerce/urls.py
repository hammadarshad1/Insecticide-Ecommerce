from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsListView.as_view(), name="Home"),
    path('product/<pk>',views.product_view, name='Product-View'),
    path('about/', views.about, name='About'),
    path('product/search/', views.searchProduct, name='Search'),
    path('404/', views.err404, name='Error404'),
    path('product/search/not-found', views.errNotFound, name='Pr-Not-Found'),
    path('product/add-to-cart/<pk>', views.addtocart, name='Add-To-Cart'),
    path('cart/', views.product_cart, name='Cart'),
    path('cart/delete/<pk>', views.delete_cart_item, name='Delete-Cart-Item')
]