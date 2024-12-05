from django.urls import path, reverse_lazy
from .views import (IndexView,SobrenosView, EventoView, EventoDetalheView, CriarUsuario, AtividadeView, EditarUsuario,
                    PerfilUsuario, EditarEndereco, EventoListView, EventoDeleteView, EventoCreateView, AtividadeDeleteView,
                    AtividadeCreateView, CategoriaCreateView)
from rest_framework.routers import SimpleRouter
from django.contrib.auth import views as auth_views
from .views import feedback_view
from . import views


router = SimpleRouter()

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobrenos', SobrenosView.as_view(), name='sobrenos'),
    path('evento', EventoView.as_view(), name='evento'),
    path('eventos', EventoView.as_view(), name='eventos'),
    path('detalhes_eventos/<int:id>/', EventoDetalheView.as_view(), name='detalhes_eventos'),
    path('detalhes_atividade/<int:id>/', AtividadeView.as_view(), name='detalhes_atividade'),
    path('cadastro/', CriarUsuario.as_view(), name='cadastro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editardados/<int:id>/', EditarUsuario.as_view(), name='editardados'),
    path('trocarsenha/', auth_views.PasswordChangeView.as_view(template_name='trocarsenha.html',
                                                              success_url=reverse_lazy('perfil')), name='trocarsenha'),
    path('perfil/<int:id>/', PerfilUsuario.as_view(), name='perfil'),
    path('editarendereco/<int:id>/', EditarEndereco.as_view(), name='editarendereco'),
    path('feedback/', feedback_view, name='feedback'),
    path('painel/<int:id>/', EventoListView.as_view(), name='painel'),
    path('delete/<int:pk>/', EventoDeleteView.as_view(), name='delete'),
    path('create/', EventoCreateView.as_view(), name='create'),
    path('atividade_create/', AtividadeCreateView.as_view(), name='atividade_create'),
    path('atividade_delete/<int:pk>/', AtividadeDeleteView.as_view(), name='atividade_delete'),
    path('categoria_create/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('inscrever_atividade/<int:id>/', views.inscrever_atividade, name='inscrever_atividade'),

]


