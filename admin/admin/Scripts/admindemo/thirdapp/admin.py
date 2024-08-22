from django.contrib import admin
from .models import Project
# Register your models here.

class Projectadmin(admin.ModelAdmin):
    list_display=['id','project_name','project_status','emp','client']
admin.site.register(Project,Projectadmin)