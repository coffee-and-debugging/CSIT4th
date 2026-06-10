from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is Home Page")

def create_blog(request):
    return HttpResponse("Let's cook something!")

def edit_blog(request):
    return HttpResponse("Ugh, i want to make some changes!")

def blog(request, blog_id):
    return HttpResponse(f'Blog id: {blog_id}')
