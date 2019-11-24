from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('product/<pk>',views.product_view, name='Product-View'),
    path('about/', views.about, name='About'),
    path('product/search/', views.searchProduct, name='Search')
]