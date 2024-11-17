from django import forms
from django.contrib.auth.models import User

class CadastroForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar Senha")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        return password2
