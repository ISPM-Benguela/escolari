from django.db import models
from django.contrib.auth.models import User
from estudantes.models import Estudantes


class Prestacao(models.Model):
    usuario = models.OneToOneField(Estudantes)
    prestacao = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Prestacao"
        verbose_name_plural = "Prestacoes"

    def __str__(self):
        return "%s" % self.prestacao
    
    def get_prestacao(self):
        return "%s " % self.prestacao
