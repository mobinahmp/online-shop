from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('PRODUCT/', views.product, name='product'),
    path('CONTACT/', views.contact,name='contact'),
    path('CHECKOUT/', views.checkout,name='checkout'),
    path('CART/', views.cart,name='cart'),
]