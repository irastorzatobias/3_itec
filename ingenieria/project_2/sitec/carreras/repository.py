from .models import Carrera, Materia


class CarreraRepository:

    def get_all_carreras(self) -> Carrera.objects:
        return Carrera.objects.all()

    def create_carrera(self, nombre: str, duracion: int) -> Carrera:
        return Carrera.objects.create(nombre=nombre, duracion=duracion)

    # tupla donde el primer elemento es la cantidad de cosas borradas, el segundo son los objetos en si,
    def delete_carrera(self, carrera_id: int) -> tuple:
        return Carrera.objects.get(id=carrera_id).delete()

    def edit_carrera(self, carrera_id: int, nombre: str, duracion: int) -> Carrera:
        carrera = Carrera.objects.get(id=carrera_id)
        carrera.nombre = nombre
        carrera.duracion = duracion
        carrera.save()

        return carrera
