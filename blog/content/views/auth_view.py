from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as Login
from ..models import Blog

def login(request):
    if request.method=="POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        
        user= authenticate(request, username=username, password=password)
        
        if user is None:
            return redirect("login")
        else:
            Login(request, user)
            return redirect("home")
          
    return render(request, 'auth/login.html')



def register(request):
    if request.method == "POST":
        username= request.POST.get("username")
        email= request.POST.get("email")
        password= request.POST.get("password")
        user= User(username=username, email=email)
        user.set_password(password)
        user.save()
        return redirect("login")
    
    return render(request, "auth/register.html")
        
