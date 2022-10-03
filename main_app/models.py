from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
#imports dates so we can calculate times between waterings
from datetime import datetime
# Create your models here.

class DbPlant(models.Model):
    common_name = models.CharField(max_length=50)
    botanical_name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    time_till_dry = models.IntegerField()
    #DB INFO ONLY
    added_at = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.common_name

    def get_absolute_url(self):
        return reverse('plant_details', kwargs={'plant_id': self.id})


class OwnedPlant(models.Model):
    type = models.ManyToManyField(DbPlant)
    nickname = models.CharField(max_length=50)
    public=  models.BooleanField(default = False)
    healthy=  models.BooleanField(default = True)
    watered = models.BooleanField (default = False)
    #time_till_dry = models.IntegerField()
    watering_date = models.DateField(auto_now_add=True)
    adopted_since = models.DateField(auto_now_add=True)
    comments = models.TextField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('plant_details', kwargs={'plant_id': self.id})