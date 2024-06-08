from django.shortcuts import render , HttpResponse

def travel(request):
    return  render(request,'travel.html')

def sport(request):
    return  render(request,'sport.html')

def Beauty_and_health(request):
    return  render(request,'Beauty_and_health.html')

def book_and_writing(request):
    return  render(request,'book_and_writing.html')

def camera(request):
    return  render(request,'camera.html')

def digital_good(request):
    return  render(request,'digital_good.html')

def food(request):
    return  render(request,'food.html')

def mobile(request):
    return  render(request,'mobile.html')

def home_and_kitchen(request):
    return  render(request,'home_and_kitchen.html')

def motor(request):
    return  render(request,'motor.html')

def Tools_and_equipment(request):
    return  render(request,'Tools_and_equipment.html')

def toy(request):
    return  render(request,'toy.html')
