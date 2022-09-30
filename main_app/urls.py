from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #auth
    path('accounts/signup/', views.signup, name='signup'),

    path ('about/', views.about, name="about"),
    path ('plants/', views.plants_index, name = "plants_index"),
    
    path ('plantsdb/', views.DbPlants_index, name = "plantsDB_index"),
    
    path ('socialfeed/', views.social_plants_feed, name = "social_plants_feed"),

    #class paths are passed .as_view() to render the class defaults
    path ('plants/add', views.OwnedPlantAdd.as_view(), name ="plant_add"),
    path ('plants/create', views.DbPlantCreate.as_view(), name ="plant_create")
]