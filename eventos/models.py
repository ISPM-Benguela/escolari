from django.db import models

class Eventos(models.Model):
    titulo = models.CharField(max_length=255)
    imagem = models.FileField(upload_to="eventos/", blank=True)
    data_inicio = models.DateTimeField()
    data_termino = models.DateField()

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return "%s" % format(self.titulo)