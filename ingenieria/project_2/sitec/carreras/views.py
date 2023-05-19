from django.shortcuts import render
from django.http.response import HttpResponse

from .repository import CarreraRepository

# Create your views here.


def index_view(request):
    return HttpResponse('index')


def carrera_view(request):
    repository = CarreraRepository()
    carreras = repository.get_all_carreras()

    return render(
        request,
        'carreras/index_carreras.html',
        {
            'carreras': carreras
        }
    )


def materias_view(request):
    return HttpResponse("Hola, soy la vista de materias")
