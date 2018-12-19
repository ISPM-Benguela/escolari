from django.conf.urls import url , include

from salas import views as visao

urlpatterns = [
    url(r'^$', visao.todos, name="turmas"),
    url(r'^cadastrar/', visao.cadastrar_turma , name="cadastrturma"),
    url(r'^visualizar/(?P<turma>[-\w]+)/$', visao.visualizar_turma, name="turmavisual"),
]
