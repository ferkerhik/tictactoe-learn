from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.decorators import  login_required
from . import  views

urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.index , name="index"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup_view, name="signup"),
    path('crate_game/', views.createGame, name='crateGame'),
    path('profile/', views.profile, name='profile'),
    path('learn/', views.learn, name='learn'),
    path('learn_ttt/', views.learn_ttt, name='learn_ttt'),
    path('learn_profile/', views.learn_profile, name='learn_profile')
]
