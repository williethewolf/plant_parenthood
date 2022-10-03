from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#I don;t think we need it but I leave it here as a concept. I think instead of using
#a custom form a simple button on a form on the view will work
######## from .forms import WateringForm #########

#import form for authetication signup
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
#user display and management
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
from django.contrib.auth.mixins import LoginRequiredMixin # research StaffuserRequiredMixin

# custom models being used
from .models import DbPlant, OwnedPlant

#for the photo implementation
#from plantparenthood.settings import ACCES_KEY, ACCESS_ID

# import uuid
# import boto3

#Remove this line for clean up once we implement the proper views renders
from django.http import HttpResponse




# User authentication
def signup(request):
    #Define taks for handling POST request
    form = UserCreationForm()
    error_message = ''
    if request.method == 'POST':
        #capture form inputs from user creation form
        form = UserCreationForm(request.POST)
        #validate the form inputs
        if form.is_valid():
            # save the input values as a new user to the database
            user = form.save()
            #programmatically log the user in
            login(request, user)
            #redirect user to the index page
            return redirect('plants_index')
        #if form is invalid, handle error
        else:
            error_message = 'Invalid credentials'
    #Define taks for handling GET request
    context = {'form': form, 'error_messages' : error_message}
    #render template with empty form
    return render(request, 'registration/signup.html', context)

# Define the home view
def home(request):
  return render(request, 'home.html', {'page_name': 'Home'})

def about(request):
  return render(request, 'about.html', {'page_name': "About"} )

 # User interaction with DB 
def DbPlants_index(request):
 #IN THE BASE HTML, THE USER HAS TO BE CHECKED AGAINST TO OLY SHOW BOTH PUBLIC FEED AND THE DB
   plants = DbPlant.objects.filter(published = True)
   return render(request, 'plants/plants_index.html', { 'page_name' : 'Plant Parenthood Plant Database', 'plants':plants} )

def social_plants_feed(request):
  return HttpResponse('<h1>Plants Social feed</h1>')


def plants_index(request):
  if request.user:
    plants = OwnedPlant.objects.filter(user = request.user)
    return render (request, 'plants/plants_index.html', { 'page_name' : 'My Owned Plants', 'plants':plants} )

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

def update_watering_date(request, plant_id, date_today):
  OwnedPlant.objects.get(ID=plant_id).update(watering_date=date_today)
  return redirect('plant_details', plant_id=plant_id)

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