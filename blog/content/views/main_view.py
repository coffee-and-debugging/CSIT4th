from django.shortcuts import render, redirect, get_object_or_404
from ..models import Blog

def home(request):
    blogs= Blog.objects.all().order_by('-created_at')
    return render(request, "main/home.html", {"blogs": blogs})

def create_blog(request):
    if request.method == "POST":
        title= request.POST.get("title")
        subtitle= request.POST.get("subtitle")
        description= request.POST.get("description")
        image= request.FILES.get("image")

        blog = Blog(title=title, subtitle=subtitle, image=image, description=description, author=request.user)
        blog.save()
        return redirect("home")

    return render(request, "main/create_blog.html")

def edit_blog(request):
    blog_id= request.GET.get("id")
    blog= get_object_or_404(Blog, id=blog_id)

    if request.method == "POST":
        blog.title= request.POST.get("title", blog.title)
        blog.subtitle= request.POST.get("subtitle", blog.subtitle)
        blog.description= request.POST.get("description", blog.description)
        if request.FILES.get("image"):
            blog.image= request.FILES.get("image")
        blog.save()
        return redirect("home")

    return render(request, "main/edit_blog.html", {"blog": blog})

def blog(request, blog_id):
    blog= get_object_or_404(Blog, id=blog_id)
    return render(request, "main/blog.html", {"blog": blog})

def terms_and_conditions(request):
    return render(request, "main/terms_and_conditions.html")
