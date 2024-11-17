from django.views.generic import ListView
from .models import Evento
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Feedback

def index(request):
    return render(request, 'index.html')
class EventosView(ListView):
    model = Evento
    template_name = 'eventos.html'
    context_object_name = 'eventos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})
def lista_atividades(request):
    atividades = Evento.objects.all()
    return render(request, 'eventos.html', {'atividades': atividades})


class FeedbackView(ListView):
    model = Feedback
    template_name = 'feedback.html'
    context_object_name = 'eventos'
