from django.shortcuts import render , HttpResponse

def loginpage(request):
    return  render(request,'login.html')

def signuppage(request):
    return  render(request,'signup.html')