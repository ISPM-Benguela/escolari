# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-09 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prestacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestacao',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='estudantes.Estudantes'),
        ),
    ]
