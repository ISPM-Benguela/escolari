# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-05 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('noBI', models.CharField(max_length=100)),
                ('candidatura', models.CharField(blank=True, choices=[('F', 'Funcionario'), ('E', 'Estudante')], default='E', max_length=1, null=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('novo', models.BooleanField(default=True)),
                ('enviado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Candidatura',
                'verbose_name_plural': 'cadidaturas',
            },
        ),
    ]
