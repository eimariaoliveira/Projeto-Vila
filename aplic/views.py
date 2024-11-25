from django.shortcuts import render, redirect, reverse
from .forms import UsuarioCreationForm
from django.views.generic import TemplateView, FormView, UpdateView
from .models import Evento, Atividade, Usuario
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['eventos'] = Evento.objects.order_by('-id').all()
        return context

class EventoView(TemplateView):
    template_name = 'evento.html'

    def get_context_data(self, **kwargs):
        context = super(EventoView, self).get_context_data(**kwargs)
        context['eventos'] = Evento.objects.all()
        return context

class EventoDetalheView(LoginRequiredMixin, TemplateView):
    template_name = 'detalhes_eventos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['id']
        context['evento'] = Evento.objects.get(id=id)
        context['atividades'] = context['evento'].atividades.all()
        return context

class AtividadeView(LoginRequiredMixin, TemplateView):
    template_name = 'detalhes_atividade.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['id']
        context['atividade'] = Atividade.objects.get(id=id)
        return context


class UsuariosView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user
        return context



class CriarUsuario(FormView):
    template_name = 'cadastro.html'
    form_class = UsuarioCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid

    def get_success_url(self):
        return reverse('login')

class EditarUsuario(LoginRequiredMixin, UpdateView):
    template_name = 'editardados.html'
    model = Usuario
    fields = ['username', 'email', 'first_name', 'last_name', 'telefone', 'cpf']

    def get_object(self, queryset=None):
        # Buscar o objeto usando o parâmetro 'id' passado na URL
        return self.model.objects.get(pk=self.kwargs['id'])

    def get_success_url(self):
        return reverse('index') #mudar para pagina do perfil











