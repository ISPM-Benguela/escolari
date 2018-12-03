from django.db import models

class AnoLectivo(models.Model):
    ano = models.DateTimeField()

    class Meta:
        verbose_name = "Ano Lectivo"
        verbose_name_plural = "Ano lectivo"
    def __str__(self):
        return sefl.ano

