from django.urls import path

from .views import carrera_view, delete_carrera_view, materias_view, index_view

urlpatterns = [
    path('', index_view, name="view"),
    path('carreras/', carrera_view, name="carreras"),
    path('carreras/delete/<int:id>', delete_carrera_view, name="delete_carrera"),
    path('materias/', materias_view, name="materias"),
]
