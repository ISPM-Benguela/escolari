# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-08 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propinas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propinas',
            name='total_propinas',
            field=models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Valor da propina'),
        ),
    ]
