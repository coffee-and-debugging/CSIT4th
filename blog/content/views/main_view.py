from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from ..models import Blog, Profile

def home(request):
    query = request.GET.get("q", "")
    blogs = Blog.objects.filter(title__icontains=query).order_by('-created_at') if query else Blog.objects.all().order_by('-created_at')
    page = Paginator(blogs, 5).get_page(request.GET.get("page"))
    return render(request, "main/home.html", {"blogs": page, "query": query})

@login_required(login_url='login')
def create_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        subtitle = request.POST.get("subtitle")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        Blog(title=title, subtitle=subtitle, image=image, description=description, author=request.user).save()
        return redirect("home")
    return render(request, "main/create_blog.html")

@login_required(login_url='login')
def edit_blog(request):
    blog_id = request.GET.get("id")
    blog = get_object_or_404(Blog, id=blog_id)
    if blog.author != request.user:
        return redirect("home")
    if request.method == "POST":
        blog.title = request.POST.get("title", blog.title)
        blog.subtitle = request.POST.get("subtitle", blog.subtitle)
        blog.description = request.POST.get("description", blog.description)
        if request.FILES.get("image"):
            blog.image = request.FILES.get("image")
        blog.save()
        return redirect("home")
    return render(request, "main/edit_blog.html", {"blog": blog})

def blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, "main/blog.html", {"blog": blog})

@login_required(login_url='login')
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if blog.author == request.user:
        blog.delete()
    return redirect("home")

@login_required(login_url='login')
def profile(request):
    user_profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST" and request.FILES.get("profile_picture"):
        user_profile.profile_picture = request.FILES.get("profile_picture")
        user_profile.save()
        return redirect("profile")
    blogs = Blog.objects.filter(author=request.user).order_by('-created_at')
    return render(request, "main/profile.html", {"user_profile": user_profile, "blogs": blogs})

def about(request):
    return render(request, "main/about.html")

def terms_and_conditions(request):
    return render(request, "main/terms_and_conditions.html")
