from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('TRAVEL/', views.travel,name='travel'),
    path('SPORT/', views.sport,name='sport'),
    path('BEAUTY AND HEALTH/', views.Beauty_and_health,name='Beauty_and_health'),
    path('BOOK AND WRITING/', views.book_and_writing,name='book_and_writing'),
    path('CAMERA/', views.camera,name='camera'),
    path('DIGITAL GOOD/', views.digital_good,name='digital_good'),
    path('FOOD/', views.food,name='food'),
    path('MOBILE/', views.mobile,name='mobile'),
    path('HOME AND KITCHEN/', views.home_and_kitchen,name='home_and_kitchen'),
    path('MOTOR/', views.motor,name='motor'),
    path('TOOL AND EQUIPMENT/', views.Tools_and_equipment,name='Tools_and_equipment'),
    path('TOY/', views.toy,name='toy'),
]