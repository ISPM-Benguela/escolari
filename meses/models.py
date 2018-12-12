from django.db import models

class Meses(models.Model):
    mes = models.CharField(max_length=255)

    class Meta:
        ordering = ('mes',)
        verbose_name = "Mes"
        verbose_name_plural = "Meses"

    def __str__(self):
        return self.mes
    
    def get_mes(self):
        return self.mes
