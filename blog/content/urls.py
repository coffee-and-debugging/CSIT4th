from django.urls import path
from .views.auth_view import login, register
from .views.main_view import create_blog, edit_blog, home, blog, delete_blog, profile, about, terms_and_conditions

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),

    path('', home, name="home"),
    path('create_blog/', create_blog, name="create_blog"),
    
    path('edit_blog', edit_blog, name="edit_blog"),
    path('blog/<int:blog_id>/', blog),
    path('blog/<int:blog_id>/delete/', delete_blog, name="delete_blog"),

    path('profile/', profile, name="profile"),
    path('about/', about, name="about"),
    path('terms_and_conditions/', terms_and_conditions, name="terms_and_conditions")
]