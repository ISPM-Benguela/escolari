from django.conf.urls import url , include

from meses import views as visao

urlpatterns = [
    url(r'^$', visao.todos, name="meses"),
    url(r'^cadastrar/', visao.cadastrar_mes, name="cadastrames"),
    url(r'^editar/(?P<id>[0-9]+)/$',  visao.editar_mes , name="editarmes"),
    url(r'^eliminarcurso/(?P<id>[0-9]+)/$',  visao.eliminar_mes , name="eliminarmes"),
    #url(r'^(?P<funcionario>\w+)', apresenta.sozinho, name="single"),
]
