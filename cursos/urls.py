from django.conf.urls import url , include

from cursos import views as apresenta

urlpatterns = [
    url(r'^$', apresenta.todos, name="cursos"),
    #url(r'^(?P<funcionario>\w+)', apresenta.sozinho, name="single"),
]
