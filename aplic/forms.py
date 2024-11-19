from django.contrib.auth.forms import UserCreationForm

from .models import Usuario
from django import forms


class UsuarioCreationForm(UserCreationForm):
    email = forms.EmailField()
    cpf = forms.CharField(label='CPF',max_length=11, required=False)
    telefone = forms.CharField(label='Telefone', max_length=11, required=False)
    class Meta:
        model = Usuario
        fields = ['first_name','last_name','cpf','telefone', 'email', 'username', 'password1', 'password2']
