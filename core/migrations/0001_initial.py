# Generated by Django 3.1.5 on 2021-11-12 04:25

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('area', django.contrib.gis.db.models.fields.GeometryField(null=True, srid=4326, verbose_name='Área')),
                ('ubicacion', models.CharField(max_length=200, null=True, verbose_name='Ubicación')),
            ],
            options={
                'verbose_name': 'area',
                'verbose_name_plural': 'areas',
            },
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.PositiveSmallIntegerField(default=100, primary_key=True, serialize=False, verbose_name='id')),
                ('dormitorio', models.IntegerField(default=1, verbose_name='dormitorio')),
                ('banos', models.IntegerField(default=1, verbose_name='baños')),
                ('comuna', models.IntegerField(default=1, verbose_name='Comuna')),
                ('area_total', models.IntegerField(default=10, verbose_name='Area total')),
                ('area_construida', models.IntegerField(default=10, verbose_name='Area construida')),
                ('tipo_propiedad', models.IntegerField(default=1, verbose_name='Tipo propiedad')),
                ('condicion', models.IntegerField(default=1, verbose_name='Condicion')),
                ('precio_tasado', models.IntegerField(default=3000, verbose_name='Precio tasado')),
                ('ubicacion', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Ubicacion')),
            ],
            options={
                'verbose_name': 'Propiedad',
                'verbose_name_plural': 'Propiedades',
            },
        ),
    ]
