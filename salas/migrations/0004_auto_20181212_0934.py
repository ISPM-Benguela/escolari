# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-12 09:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0003_auto_20181212_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turmas',
            name='responsavel',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]