from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductsListView.as_view(), name="Home"),
    path('products/<pk>',views.product_view, name='Product-View'),
    path('about/', views.about, name='About'),
    path('products/search/', views.searchProduct, name='Search'),
    path('404/', views.err404, name='Error404'),
    path('products/search/not-found', views.errNotFound, name='Pr-Not-Found'),
    path('products/add-to-cart/<pk>', views.addtocart, name='Add-To-Cart'),
    path('cart/', views.product_cart, name='Cart'),
    path('cart/delete/<pk>', views.delete_cart_item, name='Delete-Cart-Item'),
    path('product/new', views.new_product, name='New-Product'),
    path('profile/products', views.profile_products, name='Product-Profile'),
    path('category/add', views.add_category, name='Category-Add'),
]
