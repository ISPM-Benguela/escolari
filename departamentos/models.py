from django.db import models
from django.contrib.auth.models import User

class Departamentos(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    funcionario = models.ManyToManyField(User, default="", blank=True, null=True)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return self.nome
