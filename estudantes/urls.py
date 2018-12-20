from django.conf.urls import url, include

from estudantes import views as visao

urlpatterns = [

    url(r'^$', visao.inicio, name="estudantes"),
    url(r'^cadastrar/', visao.cadastrar_estudante , name="cadastraestudante"),
    url(r'^inserir/', visao.cadastrar_estudante , name="criarestudante"),
]
