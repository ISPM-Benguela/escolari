# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-14 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudantes',
            name='sobre_nome',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='estudantes',
            name='telefone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
