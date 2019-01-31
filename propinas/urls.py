from django.conf.urls import url, include

from propinas import views as visao

urlpatterns = [

    url(r'^$', visao.inicio, name="propinas"),
    url(r'^pagar/(?P<num>[0-9]+)/$', visao.pagar_propinas , name="pagarpropina"),
    url(r'^pagamento/', visao.cadastrar_pagamento , name="pagamento"),
]
