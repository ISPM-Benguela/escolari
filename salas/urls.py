from django.conf.urls import url , include

from salas import views as visao

urlpatterns = [
    url(r'^$', visao.todos, name="turmas"),
    url(r'^cadastrar/', visao.cadastrar_turma , name="cadastrturma"),
    url(r'^cadastrar-estundante/', visao.cadastrar_estudante_turma , name="turmacadastraestudante"),
    url(r'^visualizar/(?P<num>[0-9]+)/$', visao.visualizar_turma, name="turmavisual"),
    url(r'^eliminar/(?P<num>[0-9]+)/$', visao.eliminar_turma, name="turmaelimina"),
    url(r'^editar/(?P<num>[0-9]+)/$', visao.editar_turma, name="turmaedita"),
]
