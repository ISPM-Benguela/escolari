# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-09 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0006_auto_20190207_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turmas',
            name='numero_sala',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Número da sala'),
        ),
    ]
