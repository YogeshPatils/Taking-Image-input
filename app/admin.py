from django.contrib import admin
from .models import BikeModel
# Register your models here.
 
@admin.register(BikeModel)
class BikeAdmin(admin.ModelAdmin):
    list_display=['name','price','image']