from django.conf.urls import url 
from mensagem import views as visao

urlpatterns = [

    url(r'^$', visao.inicio, name="mensagem"),
    url(r'^marcar/(?P<num>[0-9]+)/$', visao.marcar_lido , name="marcar"),
   # url(r'^cadastrar/', visao.cadastrar_anolectivo , name="cadastranolectivo"),
    #url(r'^editar/(?P<nome>[-\w]+)/$', visao.editar_anolectivo , name="editarano"),
   # url(r'^eliminar/(?P<nome>[-\w]+)/$', visao.eliminar_anolectivo , name="eliminarano"),
   # url(r'^actualizar/(?P<num>[0-9]+)/$', visao.actualizar_anolectivo , name="actualizaranolectivo"),
]
