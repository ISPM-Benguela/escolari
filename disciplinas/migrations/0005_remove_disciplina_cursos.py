# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-13 05:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplinas', '0004_auto_20190105_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='cursos',
        ),
    ]
