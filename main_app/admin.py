from django.contrib import admin

# Register your models here.
from .models import  DbPlant, OwnedPlant
# admin.site.register(DbPlant)
admin.site.register(OwnedPlant)

#ad actions for Admina DB manipulation

#approving user sugestions
@admin.action(description='Mark selected plants as published')
def make_published(modeladmin, request, queryset):
    queryset.update(published='t')

class DbPlantAdmin(admin.ModelAdmin):
    list_display = ['common_name', 'published']
    ordering = ['added_at']
    actions = [make_published]

admin.site.register(DbPlant, DbPlantAdmin)