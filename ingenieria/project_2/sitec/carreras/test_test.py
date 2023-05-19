import pytest

from .models import Carrera
from .repository import CarreraRepository
from .factories import CarreraFactory


def test_compare_parameters():
    assert 1 == 1


@pytest.mark.django_db
def test_get_carreras():
    carrera = CarreraFactory()
    carrera.save()

    repository = CarreraRepository()
    carreras = repository.get_all_carreras()
    assert carreras.count() == 1
    assert carreras[0].nombre == carrera.nombre


@pytest.mark.django_db
def test_create_carrera():
    repository = CarreraRepository()
    repository.create_carrera('Turismo', 2)
    carreras = repository.get_all_carreras()

    assert carreras.count() == 1
    assert carreras[0].nombre == 'Turismo'
