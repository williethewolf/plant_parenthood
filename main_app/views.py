from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from .models import Plant
#from .forms import WateringForm

#import form for authetication signup

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
from django.contrib.auth.mixins import LoginRequiredMixin # research StaffuserRequiredMixin

from .models import DbPlant, OwnedPlant

#for the photo implementation
#from plantparenthood.settings import ACCES_KEY, ACCESS_ID

# import uuid
# import boto3

#Remove this line for clean up once we implement the proper views renders
from django.http import HttpResponse


# User authentication
def signup(request):
  return HttpResponse('<h1>sign in</h1>')

def login(request):
  return HttpResponse('<h1>log in</h1>')

# Define the home view
def home(request):
  return render(request, 'home.html', {'page_name': 'Home'})

def about(request):
  return render(request, 'about.html', {'page_name': "About"} )

 # User interaction with DB 
def DbPlants_index(request):
  return HttpResponse('<h1>plants index</h1>')

def social_plants_feed(request):
  return HttpResponse('<h1>plants index</h1>')


def plants_index(request):
  return HttpResponse('<h1>plants index</h1>')

def plant_details(request):
  return HttpResponse('<h1>plants details</h1>')

def add_watering(request):
  return HttpResponse('<h1>Water Plants</h1>')

#I think we wrap all three interactions - watering, health and visibility under a single view called toggles or interactions.

# def health_toggle(request):
#   return HttpResponse('<h1>Water Plants</h1>')

# def visibility_toggle(request):
#   return HttpResponse('<h1>Water Plants</h1>')

def add_photo(request):
  return HttpResponse('<h1>Water Plants</h1>')

class OwnedPlantAdd(CreateView):
#remove above and uncomment when log ins are set up and implemented for the super users
# class PlantAdd(LoginRequiredMixin, CreateView):
    model = OwnedPlant
    fields= ("type", "nickname", "healthy")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OwnedPlantUpdate(LoginRequiredMixin, UpdateView):
#remove above and uncomment when log ins are set up and implemented for the super users    
# class PlantUpdate(LoginRequiredMixin, UpdateView):
    pass

class OwnedPlantDelete(DeleteView):
#remove above and uncomment when log ins are set up and implemented for the super users
# class PlantDelete(LoginRequiredMixin, DeleteView):
    pass

# Admin and staff interactions

class DbPlantCreate(CreateView):
#remove above and uncomment when log ins are set up and implemented for the super users
# class DbPlantCreate(LoginRequiredMixin, CreateView):
    model = OwnedPlant
    fields= ("type", "nickname", "healthy")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DbPlantUpdate(LoginRequiredMixin, UpdateView):
#remove above and uncomment when log ins are set up and implemented for the super users    
# class PlantUpdate(LoginRequiredMixin, UpdateView):
    pass

class DbPlantDelete(DeleteView):
#remove above and uncomment when log ins are set up and implemented for the super users
# class PlantDelete(LoginRequiredMixin, DeleteView):
    pass