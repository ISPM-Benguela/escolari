# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-05 11:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('nota', models.FloatField(blank=True, default=0)),
                ('cursos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cursos.Cursos')),
                ('estudante', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'disciplina',
                'verbose_name_plural': 'disciplinas',
            },
        ),
    ]
