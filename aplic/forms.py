from django.contrib.auth.forms import UserCreationForm

from .models import Usuario, Evento, Feedback, Atividade
from django import forms


class UsuarioCreationForm(UserCreationForm):
    email = forms.EmailField()
    cpf = forms.CharField(label='CPF',max_length=11, required=False)
    telefone = forms.CharField(label='Telefone', max_length=11, required=False)
    class Meta:
        model = Usuario
        fields = ['first_name','last_name','cpf','telefone', 'email', 'username', 'password1', 'password2']


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'descricao', 'data_inicio', 'imagem']
        widgets = {
            'data_inicio': forms.DateTimeInput(attrs={'type': 'date-local'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }


class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['evento','nome', 'descricao', 'data_inicio','hora_inicio','local','capacidade','categoria', 'imagem']
        widgets = {
            'data_inicio': forms.DateTimeInput(attrs={'type': 'date-local'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'Time-local'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['atividade', 'inscricao', 'comentario', 'nota']
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'placeholder': 'Digite seu comentário...'}),
            'nota': forms.NumberInput(attrs={'min': 0, 'max': 10}),
        }
        labels = {
            'atividade': 'Atividade',
            'inscricao': 'Inscrição',
            'comentario': 'Comentário',
            'nota': 'Nota (0 a 10)',
        }

