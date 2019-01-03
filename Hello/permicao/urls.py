from django.conf.urls import url, include

from permicao import views as visao
 
urlpatterns = [

    url(r'^$', visao.inicio, name="permicsao"),
    

]
