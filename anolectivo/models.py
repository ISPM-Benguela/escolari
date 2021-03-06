from django.db import models
import datetime

class AnoLectivo(models.Model):
    ano = models.PositiveIntegerField(default="2019")
    criado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ano Lectivo"
        verbose_name_plural = "Anos Lectivos"
        ordering = ['criado']
    
    def __str__(self):
        return "%s" % self.ano
