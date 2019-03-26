# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-23 04:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=25, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('file_name', models.CharField(blank=True, max_length=200)),
                ('annotation_result', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Annotation Data',
            },
        ),
        migrations.CreateModel(
            name='PolygonCoordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cords', models.TextField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'verbose_name_plural': 'Polygon Coordinates',
            },
        ),
        migrations.AddField(
            model_name='annotationdata',
            name='poly_cords',
            field=models.ManyToManyField(to='Annotate.PolygonCoordinates'),
        ),
    ]
