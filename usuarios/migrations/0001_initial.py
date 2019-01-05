# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-05 11:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('disciplinas', '0001_initial'),
        ('propinas', '0001_initial'),
        ('departamentos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('salas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='Primeiro nome')),
                ('segundo_nome', models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='Segundo nome')),
                ('tipo_perfil', models.CharField(blank=True, choices=[('A', 'Administrador'), ('F', 'Funcionario'), ('E', 'Estudante'), ('P', 'Professor')], default='F', max_length=1, null=True, verbose_name='Tipo de peerfil')),
                ('morada', models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='nome da turma')),
                ('foto', models.FileField(blank=True, default='perfil/default.jpg', null=True, upload_to='perfil/')),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='departamentos.Departamentos')),
                ('disciplina', models.ManyToManyField(blank=True, to='disciplinas.Disciplina')),
                ('propinas', models.ManyToManyField(blank=True, to='propinas.Propinas')),
                ('turma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='salas.Turmas')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
