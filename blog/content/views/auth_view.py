from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as Login
from ..models import Profile

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
        username = request.POST.get("username")
        full_name = request.POST.get("full_name", "")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User(username=username, email=email, first_name=full_name)
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user, profile_picture=request.FILES.get("profile_picture"))
        return redirect("login")

    return render(request, "auth/register.html")
        
