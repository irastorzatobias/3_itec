from django.contrib import admin

from .models import (Carrera, Materia)
# Register your models here.


class CarreraAdmin(admin.ModelAdmin):
    model = Carrera
    list_display = ('nombre', 'duracion')


class MateriaAdmin(admin.ModelAdmin):
    model = Materia
    list_display = ('nombre', 'carrera', 'duracion')


admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Materia, MateriaAdmin)
