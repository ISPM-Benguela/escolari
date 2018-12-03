from django.db import models

#from turmas.models import Turmas

#from turmas.models import Turmas

from salas.models import Turmas

class Cursos(models.Model):
    curso = models.CharField(max_length=255)
    turma = models.ManyToManyField(Turmas, null=True, blank=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.curso
