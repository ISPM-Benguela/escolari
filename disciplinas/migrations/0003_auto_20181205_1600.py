# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-05 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplinas', '0002_auto_20181205_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='nota',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
