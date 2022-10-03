from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #auth
    path('registration/signup/', views.signup, name='signup'),

    path ('about/', views.about, name="about"),
# VIEW
    path ('plants/', views.plants_index, name = "plants_index"),
    path ('plantsdb/', views.dbPlants_index, name = "plantsDB_index"),
    
    path ('socialfeed/', views.social_plants_feed, name = "social_plants_feed"),
# DETAILS
    path ('plants/<int:plant_id>', views.plant_details, name = "plant_details"),
    path ('plantsdb/<int:plant_id>', views.dbplant_info, name = "plant_details"),

#water plants
    path ('plants/<int:plant_id>/update_watering_date/<today>', views.update_watering_date, name = 'update_watering_date'),


    #class paths are passed .as_view() to render the class defaults
    path ('plants/add', views.OwnedPlantAdd.as_view(), name ="plant_add"),
    path ('plants/create', views.DbPlantCreate.as_view(), name ="plant_create")
]