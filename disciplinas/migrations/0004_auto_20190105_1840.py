# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-05 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
        ('disciplinas', '0003_disciplina_estudante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='cursos',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='cursos',
            field=models.ManyToManyField(blank=True, null=True, to='cursos.Cursos'),
        ),
    ]
