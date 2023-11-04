from django.contrib import admin
from .models import Student , Teacher

# Register your models here.
@admin.register(Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ['teacher_name','subject']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =['id','name','roll','city']
    
    