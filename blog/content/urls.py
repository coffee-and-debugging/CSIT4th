from django.urls import path
from .views.auth_view import login, register
from .views.main_view import create_blog, edit_blog, home, blog, terms_and_conditions

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),

    path('home/', home, name="home"),
    path('create_blog/', create_blog, name="create_blog"),
    
    path('edit_blog', edit_blog, name="edit_blog"),
    path('blog/<int:blog_id>/', blog),

    path('terms_and_conditions/', terms_and_conditions, name="terms_and_conditions")
]