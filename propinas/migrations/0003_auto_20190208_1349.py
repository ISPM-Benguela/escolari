# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-08 13:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('propinas', '0002_auto_20190208_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propinas',
            old_name='estundante',
            new_name='estudante',
        ),
    ]
