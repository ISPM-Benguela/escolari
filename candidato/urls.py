from django.conf.urls import url, include

from candidato import views as visao

urlpatterns = [

    url(r'^$', visao.inicio, name="inicio"),
    url(r'^enviar/', visao.enviar_candidatura , name="enviarcandidatura"),
]
