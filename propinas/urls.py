from django.conf.urls import url, include

from propinas import views as visao

urlpatterns = [

    url(r'^$', visao.inicio, name="estudantes"),

]
