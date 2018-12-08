from django.conf.urls import url , include

from eventos import views as apresenta

urlpatterns = [  
    url(r'^$', apresenta.todos, name="eventos"),
     url(r'^cadastrar/', apresenta.cadastrar_evento, name="cadastraevento"),
    #url(r'^editar/(?P<nome>[-\w]+)/$', apresenta.editar_funcionario , name="editarusuario"),
    # url(r'^actualizar/(?P<nome>[-\w]+)/$', apresenta.editar_funcionario , name="editarfuncionario"),
    #url(r'^(?P<funcionario>\w+)', apresenta.sozinho, name="single"),
]
