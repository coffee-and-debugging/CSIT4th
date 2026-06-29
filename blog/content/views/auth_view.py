from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

def login(request):
    return render(request, "auth/login.html")

def register(request):
    if request.method == "POST":
        username= request.POST.get("username")
        email= request.POST.get("email")
        password= request.POST.get("password")
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return redirect("login")
    
    return render(request, "auth/register.html")
