from django.shortcuts import render , HttpResponse

def index(request):
    return  render(request,'index.html')

def product(request):
    return  render(request,'product.html')

def contact(request):
    return  render(request,'contact.html')

def checkout(request):
    return  render(request,'checkout.html')

def cart(request):
    return  render(request,'cart.html')