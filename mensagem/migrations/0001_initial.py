# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-05 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=13)),
                ('assunto', models.CharField(max_length=255)),
                ('mensagem', models.TextField()),
                ('por_ler', models.BooleanField(default=True)),
                ('enviado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Mensagem',
                'verbose_name_plural': 'Mengens',
            },
        ),
    ]
