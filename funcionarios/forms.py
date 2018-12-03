from django import forms
from django.contrib.auth.models import User
from usuarios.models import Perfil



class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Perfil 
        fields = ("user","primeiro_nome","segundo_nome","tipo_perfil","morada","foto")
