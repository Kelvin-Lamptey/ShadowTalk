from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('home/', views.home, name='home'),
    path('matchmaker/', views.matchmaker, name='matchmaker'),
    path('random-users/', views.random_users, name='random_users'),
    path('nearby-users/', views.nearby_users, name='nearby_users'),
    path('same-school/', views.same_school, name='same_school'),
] 