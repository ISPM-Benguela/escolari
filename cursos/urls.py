from django.conf.urls import url , include

from cursos import views as visao

urlpatterns = [
    url(r'^$', visao.todos, name="cursos"),
    url(r'^cadastrar/', visao.cadastrar_curso, name="cadastracurso"),
    url(r'^editar/(?P<id>[0-9]+)/$',  visao.editar_curso , name="editarcurso"),
    url(r'^eliminarcurso/(?P<id>[0-9]+)/$',  visao.eliminar_curso , name="eliminarcurso"),
    #url(r'^(?P<funcionario>\w+)', apresenta.sozinho, name="single"),
]
