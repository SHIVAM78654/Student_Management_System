from django.contrib import admin
from .models import Stundent

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','Fname','Lname','username','password','branch','rollno','contactno']
admin.site.register(Stundent, StudentAdmin)