from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile_page/', views.profile_page, name='profile_page'),
    path('posting/', views.posting, name='posting'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
]