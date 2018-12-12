from django.conf.urls import url 
from anolectivo import views as visao

urlpatterns = [

    url(r'^$', visao.inicio, name="ano"),
    url(r'^cadastrar/', visao.cadastrar_anolectivo , name="cadastranolectivo"),
]
