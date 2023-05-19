from .models import Carrera, Materia


class CarreraRepository:

    def get_all_carreras(self) -> Carrera.objects:
        return Carrera.objects.all()

    def create_carrera(self, nombre: str, duracion: int) -> Carrera:
        return Carrera.objects.create(nombre=nombre, duracion=duracion)
