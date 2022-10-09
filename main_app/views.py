from multiprocessing import current_process
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

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
from .models import DbPlant, OwnedPlant, Photo

#for the photo implementation
#from plantparenthood.settings import ACCES_KEY, ACCESS_ID

import uuid
import boto3

S3_Base_URL = 'https://s3.us-west-1.amazonaws.com/'
Bucket = 'cat-collector-eric-photos'

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
def dbPlants_index(request):
 #IN THE BASE HTML, THE USER HAS TO BE CHECKED AGAINST TO ONLY SHOW BOTH PUBLIC FEED AND THE DB
    plants = DbPlant.objects.filter(published = True)
    return render(request, 'plants/dbindex.html', { 'page_name' : 'Plant Database', 'plants':plants} )

def social_plants_feed(request):
    plants = OwnedPlant.objects.filter(public = True)
    return render(request, 'plants/social_feed.html', { 'page_name' : 'Social Feed', 'plants':plants} )



def plants_index(request):
  if request.user:
    plants = OwnedPlant.objects.filter(user = request.user)
    return render (request, 'plants/index.html', { 'page_name' : 'My Owned Plants', 'plants':plants} )

def plant_details(request, plant_id):
    plant = OwnedPlant.objects.get(id=plant_id)
    return render (request, 'plants/details.html', {'page_name':'Plant Details', 'plant': plant})

def dbplant_info(request, plant_id):
    plant = DbPlant.objects.get(id=plant_id)
    return render (request, 'plants/details.html', {'page_name':'Plant Info Sheet', 'plant': plant})

#INTERACTIONS
#I think we wrap all three interactions - watering, health and visibility under a single view called toggles or interactions.

def health_toggle(request, plant_id):
    current_plant = OwnedPlant.objects.get(id=plant_id)
    current_plant.healthy= not current_plant.healthy
    current_plant.save(update_fields=['healthy'])
    return redirect(request.META['HTTP_REFERER'])
    

def social_status_switch(request, plant_id):
    current_plant = OwnedPlant.objects.get(id=plant_id)
    current_plant.public = not current_plant.public
    current_plant.save(update_fields=['public'])
    return redirect(request.META['HTTP_REFERER'])

def add_photo(request):
  return HttpResponse('<h1>Add a photo</h1>')

def update_watering_date(request, plant_id, today):
  watered_plant = OwnedPlant.objects.get(id=plant_id)
  watered_plant.watering_date=today

  watered_plant.save(update_fields=['watering_date'])
  return redirect('plant_details', plant_id=plant_id)



def add_photo(request, plant_id):
    # capture the photo file from form submission
    photo_file = request.FILES.get('photo-file')
    # check if a file is present
    if photo_file:
        # initialize the boto3 s3 service
        s3 = boto3.client('s3')
        # create a unique id for each photo file
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # attempt to upload the file asset to AWS s3
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # generate a url based on the returned value of uploading to AWS
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            # associate the cat to the new photo instance
            photo = Photo(url=url, plant_id=plant_id)
            photo.save()
            # store the url as a value in the photo url attribute
        except Exception as error:
            print('An error has occurred')
            print(error)
    return redirect('plant_details', plant_id=plant_id)

#CLASS BASED VIEWS
class OwnedPlantAdd(LoginRequiredMixin, CreateView):
    model = OwnedPlant
    fields= ("type", "nickname",)

    def get_success_url(self):
        return reverse('plant_details', kwargs={'plant_id':self.object.pk})
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OwnedPlantUpdate(LoginRequiredMixin, UpdateView):
#remove above and uncomment when log ins are set up and implemented for the super users    
# class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = OwnedPlant
    fields = ("type", "nickname", "watering_date", "adopted_since", "comments")

class OwnedPlantDelete(DeleteView):
#remove above and uncomment when log ins are set up and implemented for the super users
# class PlantDelete(LoginRequiredMixin, DeleteView):
    model = OwnedPlant
    success_url = '/plants/'

# Admin and staff interactions

class DbPlantCreate(LoginRequiredMixin, CreateView):
    model = DbPlant
    fields= ("common_name", "botanical_name", "description", "time_till_dry")

    def get_success_url(self):
        return reverse('plantdb_info', kwargs={'plant_id':self.object.pk})
    
    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)
    
   
# MANAGEABLE FROM THE ADMIN PANEL - COMMENTED OUT FOR NOW

# class DbPlantUpdate(LoginRequiredMixin, UpdateView):
# #remove above and uncomment when log ins are set up and implemented for the super users    
# # class PlantUpdate(LoginRequiredMixin, UpdateView):
#     pass

# class DbPlantDelete(DeleteView):
# #remove above and uncomment when log ins are set up and implemented for the super users
# # class PlantDelete(LoginRequiredMixin, DeleteView):
#     pass