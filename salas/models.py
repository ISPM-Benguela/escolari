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


    nome = models.CharField('Nome da sala',max_length=255)
    numero_sala = models.IntegerField('Número da sala',default=0, blank=True, null=True)
    curso = models.ForeignKey(Cursos, blank=True, null=True)
    ano = models.ForeignKey(AnoLectivo, blank=True, null=True)
    nivel = models.ForeignKey(Nivel, blank=True, null=True)
    responsavel = models.ForeignKey(User, blank=True, null=True)
    periodo = models.CharField('Periodo da turma', max_length=1, choices=PERI, default=ESCOLHER,  blank=True, null=True)

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "turmas"
        
    def __str__(self):
        return "turma: %s, curso: %s, periodo: %s" % (self.nome, self.curso, self.get_periodo())
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

   
    def get_periodo(self):
        if self.periodo == 'M':
            return "Manha"
        elif self.periodo == 'N':
            return "Noite"
        elif self.periodo == 'T':
            return "Tarde"
        else:
            return "Nao definido"
    
    def get_responsavel(self):
        return self.responsavel
        
