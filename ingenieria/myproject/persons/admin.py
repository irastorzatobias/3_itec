from django.contrib import admin
from .models import Student, Carrer
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'email', 'age', 'date_of_birth', 'carrer']


@admin.register(Carrer)
class CarrerAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration']
