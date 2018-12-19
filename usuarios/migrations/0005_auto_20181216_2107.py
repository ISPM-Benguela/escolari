# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-16 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propinas', '0002_auto_20181216_2033'),
        ('usuarios', '0004_perfil_propinas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='propinas',
        ),
        migrations.AddField(
            model_name='perfil',
            name='propinas',
            field=models.ManyToManyField(blank=True, to='propinas.Propinas'),
        ),
    ]