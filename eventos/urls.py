from django.conf.urls import url , include

from eventos import views as apresenta

urlpatterns = [  
    url(r'^$', apresenta.todos, name="eventos"),
    url(r'^cadastrar/', apresenta.cadastrar_evento, name="cadastraevento"),
    url(r'^editar/(?P<num>[0-9]+)/$', apresenta.editar_eventos , name="editarevento"),
    url(r'^remover/(?P<num>[0-9]+)/$', apresenta.remover_eventos , name="removerevento"),
    url(r'^actualizar/(?P<num>[0-9]+)/$', apresenta.actualizar_eventos , name="actualizarevento"),
    #url(r'^(?P<funcionario>\w+)', apresenta.sozinho, name="single"),
]
