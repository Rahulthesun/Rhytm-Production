from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Playlist(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    title=models.CharField(max_length=200, null=False, blank=False)
    caption=models.TextField( null=True, blank=True)
    push=models.ManyToManyField(User ,blank=True ,related_name='push')

    embed_code=models.CharField(max_length=300)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.push.count()

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200,null=False,blank=False)
    bio=models.TextField(null=True,blank=True)
    email=models.EmailField(max_length=254)
    social=models.CharField(max_length=254,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
