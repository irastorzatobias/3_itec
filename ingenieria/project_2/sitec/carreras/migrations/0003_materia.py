# Generated by Django 4.2.1 on 2023-05-05 00:31

import carreras.choices
from django.db import migrations, models
import django.db.models.deletion
import enumchoicefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0002_alter_carrera_created_at_alter_carrera_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Materia')),
                ('duracion', enumchoicefield.fields.EnumChoiceField(default=carreras.choices.DuracionMateria['SEMESTRAL'], enum_class=carreras.choices.DuracionMateria, max_length=13)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carreras.carrera', verbose_name='Carrera')),
            ],
            options={
                'verbose_name': ('Materia',),
                'verbose_name_plural': ('Carreras',),
                'unique_together': {('nombre', 'carrera')},
            },
        ),
    ]
