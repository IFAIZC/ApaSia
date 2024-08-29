from django.contrib import admin
from .models import UserProfile, Posting

admin.site.register(UserProfile)
admin.site.register(Posting)