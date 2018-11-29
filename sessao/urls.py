from django.conf.urls import url
from django.contrib.auth.views import login

urlpatterns = [
    #url(r'^$', login, {'template_name' : {'template_name': 'sessao/entrar.html'}, name = 'entrar'),
    url(r'^$', login, {'template_name': 'sessao/entrar.html'},
        name='entrar'),

]
