from django.db import models
from django.contrib.auth.models import User
from cursos.models import Cursos
from disciplinas.models import Disciplina
from anolectivo.models import AnoLectivo
from nivel.models import Nivel

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


    nome = models.CharField(max_length=255)
    curso = models.ForeignKey(Cursos, blank=True, null=True)
    ano = models.ForeignKey(AnoLectivo, blank=True, null=True)
    nivel = models.ForeignKey(Nivel, blank=True, null=True)
    disciplina = models.ManyToManyField(Disciplina, blank=True)
    estudante = models.ForeignKey(User, blank=True, null=True)
    periodo = models.CharField('Tipo de peerfil', max_length=1, choices=PERI, default=ESCOLHER,  blank=True, null=True)

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "turmas"
        
    def __str__(self):
        return "turma: %s, curso: %s" % (self.nome, self.curso)
    @property
    def get_turma(self):
        return "%s" % self.nome
    @property
    def get_curso(self):
         return "%s" % self.curso
    @property
    def get_ano(self):
         return "%s" % format(self.ano)
    
    @property
    def get_nivel(self):
         return "%s" % self.nivel
