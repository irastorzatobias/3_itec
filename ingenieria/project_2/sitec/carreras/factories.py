import factory

from .models import Carrera


class CarreraFactory(factory.Factory):
    class Meta:
        model = Carrera

    nombre = "Ing. Ambiental"
    duracion = 2
