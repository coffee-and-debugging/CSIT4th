from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import Blog

def home(request):
    return render(request, "main/home.html")

def create_blog(request):
    if request.method== "POST":
        title= request.POST.get("title")
        subtitle= request.POST.get("subtitle")
        image= request.FILES.get("image")
        description= request.POST.get("description")


        blog= Blog(title=title, subtitle=subtitle, image=image, description=description)
        blog.save()

        return redirect('login')

    return render(request, "main/create_blog.html")



def edit_blog(request):
    return render(request, "main/edit_blog.html")

def blog(request, blog_id):
    return HttpResponse(f'Blog id: {blog_id}')

def terms_and_conditions(request):
    return render(request, "main/terms_and_conditions.html")
