# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-08 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propinas', '0003_auto_20190208_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='propinas',
            name='prestacao',
            field=models.IntegerField(default=0),
        ),
    ]
