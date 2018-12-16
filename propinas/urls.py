from django.conf.urls import url, include

from propinas import views as visao

urlpatterns = [

    url(r'^$', visao.inicio, name="estudantes"),
     url(r'^pagar/(?P<nome>[-\w]+)/$', visao.pagar_propinas , name="pagarpropina"),
]
