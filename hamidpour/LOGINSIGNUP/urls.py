from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('LOG IN/', views.loginpage,name='loginpage'),
    path('SIGN UP/', views.signuppage,name='signuppage'),

]