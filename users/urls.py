from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('register', views.registerUser, name='register'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
]
