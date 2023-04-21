# Create your models here.
from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    carrer = models.ForeignKey(
        'Carrer', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Carrer(models.Model):
    name = models.CharField(
        max_length=50, verbose_name='Carreras')

    duration = models.IntegerField(
        verbose_name='Duracion')

    def __str__(self):
        return self.name
