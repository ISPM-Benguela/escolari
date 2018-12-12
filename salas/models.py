from django.db import models
from django.contrib.auth.models import User
from cursos.models import Cursos
from disciplinas.models import Disciplina

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
    curso = models.ForeignKey(Cursos, blank=True, null=True)
    disciplina = models.ManyToManyField(Disciplina, blank=True)
    responsavel = models.OneToOneField(User, blank=True)
    periodo = models.CharField('Tipo de peerfil', max_length=1, choices=PERI, default=ESCOLHER,  blank=True, null=True)

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "turmas"
        
    def __str__(self):
        return " %s" % self.turma

    def get_turma(self):
        return "%s" % self.c
    
    def get_curso(self):
         return "%s" % self.curso
