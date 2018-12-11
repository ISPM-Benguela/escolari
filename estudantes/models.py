from django.db import models
from django.contrib.auth.models import User 
from salas.models import Turmas
from usuarios.models import Perfil

class Estudantes(models.Model):
    peril = models.ForeignKey(Perfil, default="")
    turma = models.ForeignKey(Turmas, blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Estudante"
        verbose_name_plural = "Estudantes"
    
    def __str__(self):
        return self.peril.user

    