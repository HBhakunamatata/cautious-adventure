from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.user_profile, name="profile"),
    path('login/', views.goto_login, name='login-form'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('profile-update', views.profile_update, name='profile-update')
]
