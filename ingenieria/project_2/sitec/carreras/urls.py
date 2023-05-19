from django.urls import path

from .views import carrera_view, materias_view, index_view

urlpatterns = [
    path('', index_view, name="view"),
    path('carreras/', carrera_view, name="carreras"),
    path('materias/', materias_view, name="materias"),
]
