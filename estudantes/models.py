from django.db import models

class Estudantes(models.Model):
    pass 

    class Media:
        css = {
            "all" : ("css/estudante.css",)
        }
        js = ('js/estudante.js',)
