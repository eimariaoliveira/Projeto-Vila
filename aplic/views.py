from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from .forms import UsuarioCreationForm, FeedbackForm
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView, ListView, CreateView, DetailView
from .models import Evento, Atividade, Usuario, Endereco, Feedback, Categoria
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages




@login_required
def inscrever_atividade(request, id):
    atividade = get_object_or_404(Atividade, id=id)

    if request.method == 'POST':
        # Verificar se o usuário está tentando se inscrever
        if 'inscrever' in request.POST:
            # Verificar se o usuário já está inscrito
            if request.user in atividade.inscritos.all():
                messages.error(request, 'Você já está inscrito nesta atividade.')
            else:
                inscritos_count = atividade.inscritos.count()

                # Verificar se a atividade atingiu a capacidade
                if atividade.capacidade and inscritos_count >= atividade.capacidade:
                    messages.error(request, 'A atividade já atingiu a capacidade máxima.')
                else:
                    atividade.inscritos.add(request.user)

                    # Atualizar a capacidade, se necessário
                    if atividade.capacidade:
                        atividade.capacidade -= 1
                        atividade.save()

                    messages.success(request, 'Sua inscrição foi feita com sucesso!')

        # Verificar se o usuário está tentando cancelar a inscrição
        elif 'cancelar' in request.POST:
            if request.user in atividade.inscritos.all():
                atividade.inscritos.remove(request.user)

                # Atualizar a capacidade, se necessário
                if atividade.capacidade is not None:
                    atividade.capacidade += 1
                    atividade.save()

                messages.success(request, 'Sua inscrição foi cancelada com sucesso!')
            else:
                messages.error(request, 'Você não está inscrito nesta atividade.')

        return redirect('detalhes_atividade', id=id)
    else:
        return redirect('detalhes_atividade', id=id)


class AtividadeView(DetailView):
    model = Atividade
    template_name = 'atividade_detalhes.html'
    context_object_name = 'atividade'

    def post(self, request, *args, **kwargs):
        atividade = self.get_object()

        messages.success(request, 'Sua inscrição foi feita com sucesso!')

        # Redirecionar de volta para a página de detalhes
        return redirect('detalhes_atividade', id=atividade.id)

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


class SobrenosView(TemplateView):
    template_name = 'sobrenos.html'


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')  # Redireciona após salvar
    else:
        form = FeedbackForm()

    feedbacks = Feedback.objects.all().order_by('-criado_em')  # Lista de feedbacks
    return render(request, 'feedback.html', {'form': form, 'feedbacks': feedbacks})


class CriarUsuario(FormView):
    template_name = 'cadastro.html'
    form_class = UsuarioCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')


class EditarUsuario(LoginRequiredMixin, UpdateView):
    template_name = 'editardados.html'
    model = Usuario
    fields = ['username', 'email', 'first_name', 'last_name', 'telefone', 'cpf', 'data_nascimento', 'foto']

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs['id'])

    def get_success_url(self):
        return reverse('perfil', kwargs={'id': self.request.user.id})


class EditarEndereco(LoginRequiredMixin, UpdateView):
    template_name = 'editarendereco.html'
    model = Endereco
    fields = ['logradouro', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'estado']

    def get_object(self, queryset=None):
        return self.model.objects.filter(usuario=self.request.user).first()

    def form_valid(self, form):
        # Certifica-se de que o novo endereço seja vinculado ao usuário
        if not form.instance.pk:
            form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('perfil', kwargs={'id': self.request.user.id})


class PerfilUsuario(LoginRequiredMixin, TemplateView):
    template_name = 'perfil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.request.user
        return context


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Feedback enviado com sucesso!')
            return redirect('feedback')  # Substitua 'feedback' pelo nome correto da sua URL
        else:
            messages.error(request, 'Erro ao enviar o feedback. Verifique os dados.')
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})


class EventoListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Evento
    template_name = 'painel.html'
    context_object_name = 'eventos'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name__in=['Administrador']).exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['atividades'] = Atividade.objects.all().order_by('data_inicio')
        return context


class EventoDeleteView(DeleteView):
    model = Evento
    template_name = 'delete.html'
    success_url = reverse_lazy('evento')

    def get_queryset(self):
        return Evento.objects.all()

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name__in=['Administrador']).exists()


class EventoCreateView(LoginRequiredMixin, CreateView):
    model = Evento
    template_name = 'create.html'
    fields = ['nome', 'data_inicio', 'descricao', 'imagem']
    success_url = reverse_lazy('evento')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name__in=['Administrador']).exists()


class AtividadeDeleteView(DeleteView):
    model = Atividade
    template_name = 'atividade_delete.html'
    success_url = reverse_lazy('evento')

    def get_queryset(self):
        return Atividade.objects.all()

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name__in=['Administrador']).exists()


class AtividadeCreateView(LoginRequiredMixin, CreateView):
    model = Atividade
    template_name = 'atividade_create.html'
    fields = ['evento', 'nome', 'descricao', 'data_inicio', 'hora_inicio', 'local', 'capacidade', 'categoria', 'imagem']
    success_url = reverse_lazy('evento')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name__in=['Administrador']).exists()


class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = 'categoria_create.html'
    fields = ['nome']
    success_url = reverse_lazy('evento')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name__in=['Administrador']).exists()
