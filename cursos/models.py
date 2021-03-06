from django.db import models

class Cursos(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nome
