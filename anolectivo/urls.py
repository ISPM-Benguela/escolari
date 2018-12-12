from django.conf.urls import url 
from anolectivo import views as visao

urlpatterns = [

    url(r'^$', visao.inicio, name="ano"),
    url(r'^cadastrar/', visao.cadastrar_anolectivo , name="cadastranolectivo"),
    url(r'^editar/(?P<nome>[-\w]+)/$', visao.editar_anolectivo , name="editarano"),
    url(r'^eliminar/(?P<nome>[-\w]+)/$', visao.eliminar_anolectivo , name="eliminarano"),
]
