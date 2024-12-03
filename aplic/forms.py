from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Feedback
from django import forms

class UsuarioCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
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
