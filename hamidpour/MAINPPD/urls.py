from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('CAMERA DETAIL/', views.cameradetail,name='cameradetail'),
    path('DRAIL DETAIL/', views.draildetail,name='draildetail'),
    path('GALEXY WATCH 5 DETAIL/', views.galexywatcgdetail,name='galexywatcgdetail'),
    path('IPHONE 15 DETAIL/', views.iphone15detail,name='iphone15detail'),
    path('LAMP DETAIL/', views.lampdetail,name='lampdetail'),
    path('OTG DETAIL/', views.otgdetail,name='otgdetail'),
    path('PERFUM DETAIL/', views.perfumdeatail,name='perfumdeatail'),
    path('SHAHNAME DETAIL/', views.shahnamedetail,name='shahnamedetail'),
    path('TV DETAIL/', views.tvdetail,name='tvdetail'),
    path('VOLLEYBALL DETAIL/', views.volleyballdetail,name='volleyballdetail'),
]