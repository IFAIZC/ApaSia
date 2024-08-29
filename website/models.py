from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    occupation = models.CharField(blank=True, null=True, max_length=500)
    age = models.IntegerField(blank=True, null=True)
    profile_picture = models.ImageField(null=True, blank=True) #LATEST! working on displaying profile picture. 28/8/2024 ** also, might need to change the null to something else.
    
    def __str__(self):
        return self.user.username
    
class Posting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="post_likes")
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.content[:500]
    
