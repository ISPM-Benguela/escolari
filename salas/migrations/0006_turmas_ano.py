# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-12 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anolectivo', '0001_initial'),
        ('salas', '0005_auto_20181212_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='turmas',
            name='ano',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anolectivo.AnoLectivo'),
        ),
    ]
