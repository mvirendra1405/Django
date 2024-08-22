from django.contrib import admin
from .models import Emp,Account
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=['id','name','email','contact']
    list_filter=['name','email']
admin.site.register(Emp,EmpAdmin)



class AccountAdmin(admin.ModelAdmin):
    list_display=['id','salary','month','emp']
    list_filter=['id','month']
admin.site.register(Account,AccountAdmin)