from django.db import models

# Create your models here.
class Turmas(models.Model):
    turma = models.CharField(max_length=255)