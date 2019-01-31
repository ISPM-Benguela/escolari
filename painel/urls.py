from django.conf.urls import url, include

from painel import views as visao
from usuarios import views as usuario

urlpatterns = [

    url(r'^$', visao.inicio, name="painel"),
    url(r'^perfil/(?P<num>[-\w]+)/$', usuario.perfil , name="perfil"),
    url(r'^funcionarios/', include('funcionarios.urls')),
    url(r'^disciplina/', include('disciplinas.urls')),
    url(r'^candidato/', include('candidato.urls')),
    url(r'^departamentos/', include('departamentos.urls')),
    url(r'^turmas/', include('salas.urls')),
    url(r'^estudantes/', include('estudantes.urls')),
    url(r'^propinas/', include('propinas.urls')),
    url(r'^mensagem/', include('mensagem.urls')),
    url(r'^cursos/', include('cursos.urls')),
    url(r'^nivel/', include('nivel.urls')),
    url(r'^ano/', include('anolectivo.urls')),
    url(r'^eventos/', include('eventos.urls')),
]
