from django.db import models
from django.contrib.auth.models import User
from cursos.models import Cursos

class Turmas(models.Model):

    NOITE = 'N'
    MANHA = 'M'
    TARDE= 'T'
    ESCOLHER = 'E'

    PERI = (
        (NOITE, 'Noite'),
        (MANHA, 'Manha'),
        (TARDE, 'Tarde'),
        (ESCOLHER, 'Selecionar periodo')
    )


    turma = models.CharField(max_length=255)
    curso = models.ForeignKey(Cursos)
    estudante = models.ManyToManyField(User, null=True, blank=True)
    #responsavel = models.OneToOneField(User, null = True, blank=True)
    periodo = models.CharField('Tipo de peerfil', max_length=1, choices=PERI, default=ESCOLHER,  blank=True, null=True)

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "turmas"
        
    def __str__(self):
        return self.turma