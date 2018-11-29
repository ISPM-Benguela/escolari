from django.conf.urls import url , include

from departamentos import views as apresenta

urlpatterns = [
    url(r'^$', apresenta.todos, name="departamentos"),
    url(r'^cadastrar/', apresenta.cradastrar_departamento, name="criadeparta"),
    url(r'^actualizar/(?P<nome>[-\w]+)/$', apresenta.editar_departamento, name="editardeparta"),
]
