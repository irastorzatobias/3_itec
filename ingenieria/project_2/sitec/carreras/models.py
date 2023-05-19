from django.db import models

from .choices import DuracionMateria
from enumchoicefield import EnumChoiceField

# Create your models here.


class Carrera(models.Model):
    DURACION = (
        (1, "UNO"),
        (2, "DOS"),
        (3, "TRES"),
    )

    nombre = models.CharField(
        verbose_name='Carrera',
        max_length=100,
    )

    duracion = models.IntegerField(
        verbose_name='Duracion',
        choices=DURACION,
    )

    created_at = models.DateTimeField(
        verbose_name='Creado el',
        auto_now=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Updateado el',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
        ordering = ['-created_at']

    def __str__(self):
        return self.nombre


class Materia(models.Model):
    nombre = models.CharField(
        verbose_name='Materia',
        max_length=100
    )
    carrera = models.ForeignKey(
        Carrera,
        verbose_name='Carrera',
        on_delete=models.CASCADE,
        related_name='materias',
    )
    duracion = EnumChoiceField(
        DuracionMateria,
        default=DuracionMateria.SEMESTRAL,
        verbose_name='Duración',
    )
    created_at = models.DateTimeField(
        verbose_name='Creado el',
        auto_now=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='Actualizado el',
        auto_now=True,
    )

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        ordering = ['-created_at']
        unique_together = ['nombre', 'carrera']

    def _str_(self):
        return self.nombre
