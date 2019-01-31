from django.conf.urls import url , include

from nivel import views as visao

urlpatterns = [
    url(r'^$', visao.todos, name="nivel"),
    url(r'^cadastrar/', visao.cadastrar_nivel, name="cadastranivel"),
    url(r'^editar/(?P<id>[0-9]+)/$',  visao.editar_nivel , name="editarnivel"),
    url(r'^eliminarcurso/(?P<id>[0-9]+)/$',  visao.eliminar_nivel , name="eliminarnivel"),
    #url(r'^(?P<funcionario>\w+)', apresenta.sozinho, name="single"),
]
