from django.db import models
from django.contrib.auth.models import User 
from cursos.models import Cursos

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    estudante = models.ManyToManyField(User, blank=True)
    nota = models.FloatField(default=0, blank=True)

    class Meta:
        verbose_name = "disciplina"
        verbose_name_plural = "disciplinas"

    def __str__(self):
        return self.nome