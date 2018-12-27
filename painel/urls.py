from django.conf.urls import url, include

from painel import views as visao

urlpatterns = [

    url(r'^$', visao.inicio, name="propinas"),
]
