from django.contrib import admin
from .models import Category,Product,Cart
# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','description']

admin.site.register(Category,categoryAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display=['id','p_name','p_price','p_description','Category']
admin.site.register(Product,ProductAdmin)

