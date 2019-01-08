from django.conf.urls import url, include

from disciplinas import views as visao

urlpatterns = [

    url(r'^$', visao.inicio, name="disciplinas"),
    #url(r'^cadastrar/', visao.cadastrar_estudante , name="cadastrardisciplina"),
    #url(r'^inserir/', visao.cadastrar_estudante , name="criarestudante"),
    #url(r'^visualizar/(?P<num>[0-9]+)/$', visao.visualizar_estudante , name="visualizarestudante"),
]

