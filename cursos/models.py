from django.db import models

#from turmas.models import Turmas

#from turmas.models import Turmas

from salas.models import Turmas

class Cursos(models.Model):
    curso = models.CharField(max_length=255)
    turma = models.ManyToManyField(Turmas, null=True, blank=True)
