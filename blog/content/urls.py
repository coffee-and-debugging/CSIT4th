from django.urls import path
from .views.auth_view import login, register
from .views.main_view import create_blog, edit_blog, home, blog

urlpatterns = [
    path('login/', login),
    path('register/', register),

    path('home/', home, name="home"),
    path('create_blog/', create_blog, name="create_blog"),
    
    path('edit_blog', edit_blog),
    path('blog/<int:blog_id>/', blog)
]