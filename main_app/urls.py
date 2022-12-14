from django.contrib import admin
from django.urls import path, include
from . import views

#to pass the date in the URL we need to conver it as a string using a custom path converter <date:...>
from django.urls import path, register_converter
from main_app.dateconverter import DateConverter
register_converter(DateConverter, 'date')

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
    path ('plantsdb/<int:plant_id>', views.dbplant_info, name = "plantdb_info"),
#INTERACTIONS
#water plants
    path ('plants/<int:plant_id>/update_watering_date/<date:today>', views.update_watering_date, name = 'update_watering_date'),

#make public on the social feed
    path  ('plants/<int:plant_id>/social_status_switch', views.social_status_switch, name = 'social_status_switch'),

#make public on the social feed
    path  ('plants/<int:plant_id>/health_toggle', views.health_toggle, name = 'health_toggle'),

    #class paths are passed .as_view() to render the class defaults
#ADD PLANTS
    path ('plants/add', views.OwnedPlantAdd.as_view(), name ="plant_add"),
    path ('plants/create', views.DbPlantCreate.as_view(), name ="plant_create"),
#UPDATE PLANTS
    path ('plants/<int:pk>/update/', views.OwnedPlantUpdate.as_view(), name="plant_update"),
#REMOVE PLANTS
    path ('plants/<int:pk>/delete/', views.OwnedPlantDelete.as_view(), name='plant_delete'),
# UPLOAD PHOTO
    path('plants/<int:plant_id>/add_photo/', views.add_photo, name='add_photo'),
    path('plantsdb/<int:plant_id>/add_photo/', views.add_photo, name='add_dbphoto'),
]