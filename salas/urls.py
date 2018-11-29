from django.conf.urls import url , include

from salas import views as apresenta

urlpatterns = [
    url(r'^$', apresenta.todos, name="turmas"),
    #url(r'^(?P<funcionario>\w+)', apresenta.sozinho, name="single"),
]
