from django.contrib import admin
from .models import Client
# Register your models here.


class Clientadmin(admin.ModelAdmin):
    list_display=['id','c_name','c_email','c_contact','c_age','c_address']
    list_filter=['id','c_name']
admin.site.register(Client,Clientadmin)