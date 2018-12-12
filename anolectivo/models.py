from django.db import models

class AnoLectivo(models.Model):
    ano = models.DateField()

    class Meta:
        verbose_name = "Ano Lectivo"
        verbose_name_plural = "Anos LEctivos"
    
    def __str__(self):
        return "%s" % self.ano
