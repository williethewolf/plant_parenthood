from django.contrib import admin

# Register your models here.
from .models import  DbPlant, OwnedPlant
admin.site.register(DbPlant)
admin.site.register(OwnedPlant)