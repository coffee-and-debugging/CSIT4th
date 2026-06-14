from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "main/home.html")

def create_blog(request):
    return render(request, "main/create_blog.html")

def edit_blog(request):
    return render(request, "main/edit_blog.html")

def blog(request, blog_id):
    return HttpResponse(f'Blog id: {blog_id}')
