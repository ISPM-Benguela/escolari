from django.conf.urls import url , include

from financas import views as apresenta

urlpatterns = [
    url(r'^$', apresenta.todos, name="pagamentos"),
    url(r'^cadastrar/', apresenta.cradastrar_valor_propinas, name="crpropina"),
    url(r'^editar/(?P<num>[0-9]+)/$', apresenta.editar_valor_propinas, name="upropina"),
    url(r'^elimnar/(?P<num>[0-9]+)/$', apresenta.eliminar_pagamento, name="dpropina"),
]
