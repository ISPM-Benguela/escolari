from django.db import models
from anolectivo.models import AnoLectivo

class Nivel(models.Model):
    nome = models.CharField(max_length=255)
    ano_lectivo = models.ForeignKey(AnoLectivo)

    def __str__(self):
        return "{} " .format(self.nome)

