# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-08 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Total do valor')),
                ('tipo_servico', models.CharField(blank=True, choices=[('P', 'Propina'), ('M', 'Matricula')], default='M', max_length=1, null=True, verbose_name='Tipo de perfil')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data do pagamento')),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamentos',
            },
        ),
    ]
