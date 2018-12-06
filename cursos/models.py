from django.db import models

class Cursos(models.Model):
    curso = models.CharField(max_length=255)
    #sala = models.ManyToManyField(Turmas, blank=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.curso
