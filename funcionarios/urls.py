from django.conf.urls import url , include

from funcionarios import views as apresenta

urlpatterns = [  
    url(r'^$', apresenta.todos, name="funcionarios"),
    url(r'^cadastrar/', apresenta.cadastrar_funcionario , name="cadastrafuncionario"),
    url(r'^editar/(?P<nome>[-\w]+)/$', apresenta.editar_funcionario , name="editarusuario"),
     url(r'^actualizar/(?P<nome>[-\w]+)/$', apresenta.editar_funcionario , name="editarfuncionario"),
    #url(r'^(?P<funcionario>\w+)', apresenta.sozinho, name="single"),
]
