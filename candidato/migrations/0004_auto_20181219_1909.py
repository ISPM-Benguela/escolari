# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-19 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0003_auto_20181219_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='enviado',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
