from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)

class Blog(models.Model):
    title= models.CharField(max_length=50)
    subtitle= models.CharField(max_length=100)
    image= models.ImageField(upload_to="images/")
    description= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
