# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-19 12:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidato',
            old_name='dataCandidatura',
            new_name='data',
        ),
    ]
