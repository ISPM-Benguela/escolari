from django.db import models

class Nivel(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return "%s " % self.nome

