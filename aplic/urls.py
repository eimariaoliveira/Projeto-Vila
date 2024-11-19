from django.contrib.auth.views import LoginView
from django.urls import path
from .views import IndexView, EventoView, EventoDetalheView, CriarUsuario, AtividadeView
from rest_framework.routers import SimpleRouter
from django.contrib.auth import views as auth_views


router = SimpleRouter()

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('evento', EventoView.as_view(), name='evento'),
    path('detalhes_eventos/<int:id>/', EventoDetalheView.as_view(), name='detalhes_eventos'),
    path('detalhes_atividade/<int:id>/', AtividadeView.as_view(), name='detalhes_atividade'),
    path('cadastro/', CriarUsuario.as_view(), name='cadastro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

]
