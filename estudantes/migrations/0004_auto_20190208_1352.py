# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-08 13:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudantes', '0003_auto_20190131_1856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudantes',
            old_name='peril',
            new_name='perfil',
        ),
    ]
