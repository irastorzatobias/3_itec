from django.shortcuts import render, redirect
from django.http.response import HttpResponse

from .forms import CarreraForm
from .repository import CarreraRepository


# Create your views here.


def index_view(request):
    return HttpResponse('index')


def carrera_view(request):
    repository = CarreraRepository()
    carreras = repository.get_all_carreras()
    carrera_form = CarreraForm()

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        duracion = request.POST.get('duracion')
        repository.create_carrera(nombre, duracion)
        ok = True
    else:
        ok = False

    return render(
        request,
        'carreras/index_carreras.html',
        {
            'form': carrera_form,
            'carreras': carreras,
            'ok': ok
        }
    )


def delete_carrera_view(request, id):
    repository = CarreraRepository()
    repository.delete_carrera(id)
    return redirect('carreras')


def materias_view(request):
    return HttpResponse("Hola, soy la vista de materias")
