from django.shortcuts import render, redirect, reverse
from .forms import UsuarioCreationForm
from django.views.generic import TemplateView, FormView
from django.contrib.auth.decorators import login_required
from .models import Evento, Atividade
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

class EventoDetalheView(TemplateView):
    template_name = 'detalhes_eventos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['id']
        context['evento'] = Evento.objects.get(id=id)
        context['atividades'] = context['evento'].atividades.all()
        return context

class AtividadeView(TemplateView):
    template_name = 'detalhes_atividade.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['id']
        context['atividade'] = Atividade.objects.get(id=id)
        return context




class CriarUsuario(FormView):
    template_name = 'cadastro.html'
    form_class = UsuarioCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid

    def get_success_url(self):
        return reverse('login')









