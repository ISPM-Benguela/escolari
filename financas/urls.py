from django.conf.urls import url , include

from financas import views as apresenta

urlpatterns = [
    url(r'^$', apresenta.todos, name="financas"),
   # url(r'^cadastrar/', apresenta.cradastrar_valor_propinas, name="crpropina"),
   # url(r'^editar/(?P<num>[0-9]+)/$', apresenta.editar_valor_propinas, name="upropina"),
   # url(r'^actualizar/(?P<num>[0-9]+)/$', apresenta.actualizar_departamento, name="actualizar"),
]
