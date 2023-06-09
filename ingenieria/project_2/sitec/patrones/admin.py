from django.contrib import admin

# Register your models here.
from patrones.models import (CovidInfoModel)


class CovidInfoAdmin(admin.ModelAdmin):
    model = CovidInfoModel
    list_display = ('date', 'positive', 'negative')


admin.site.register(CovidInfoModel, CovidInfoAdmin)
