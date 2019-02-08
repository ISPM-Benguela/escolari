from django.db import models
from django.contrib.auth.models import User 
from salas.models import Turmas
from usuarios.models import Perfil
from disciplinas.models import Disciplina

class Estudantes(models.Model):
    perfil = models.ForeignKey(Perfil, default="")
    turma = models.ForeignKey(Turmas, blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    primeiro_nome = models.CharField(max_length=255, blank=True, null=True)
    sobre_nome = models.CharField(max_length=255, blank=True, null=True)
    nome_encarregado = models.CharField(max_length=255, blank=True, null=True)
    propinas = models.IntegerField(default=0)
    disciplinas = models.ManyToManyField(Disciplina, blank=True)

    class Meta:
        verbose_name = "Estudante"
        verbose_name_plural = "Estudantes"
    
    def __str__(self):
        return "%s" % self.get_estudante()
    
    def get_ano(self):
        return "%s" % self.turma.ano
    
    def get_curso(self):
        return "%s" % self.turma.curso
    def get_estudante(self):
        if not self.primeiro_nome or not self.sobre_nome:
            return "%s" % self.perfil
        else:
            return "%s %s" % (self.primeiro_nome, self.sobre_nome) 
    
    def get_prestacoes(self):
        return self.propinas
    


    