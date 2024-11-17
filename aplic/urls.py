from django.urls import path
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from . import views
from .views import EventosView
from django.contrib.auth.views import LogoutView
from .views import FeedbackView



urlpatterns = [
    path("", views.index, name="index"),
    path('login/', LoginView.as_view(), name='login'),
    path('eventos/', EventosView.as_view(), name='eventos'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),


]

@login_required
def adquirir_ingresso(request):
    return render(request, 'adquirir_ingresso.html')

