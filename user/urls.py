from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('<int:id>/', views.profile_feed, name='profile-feed'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]