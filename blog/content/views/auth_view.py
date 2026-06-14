from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, "auth/login.html")

def register(request):
    return render(request, "auth/register.html")
