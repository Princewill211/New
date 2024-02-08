from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('profile/<int:pk>/', views.UserProfile, name="profile"),
    path('logout/', views.logout_user, name="logout"),
]